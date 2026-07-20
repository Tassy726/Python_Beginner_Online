# 演習⑥ ミニクイズアプリ２ 解説

【最初に】mdファイルはVSCode上で「Ctrl + Shift + V」でプレビュー表示に切り替わります。

前回、演習⑤のミニクイズアプリに対して仁礼くんから改造リクエストが出たね。

- 選択肢をラジオボタンにして三択問題にする
- 出題番号と選択肢をランダムにする
- リトライボタンを設置する

この3つを全部実装した完成版が `演習6_ミニクイズアプリ2_完成形.py`。
今回は「どう作ったか」を、コードを読みながら解説していくよ。
**穴埋めじゃなくて完成コードを読む回**なので、気になるところはどんどん質問してOK！

---

## 今日読み解くこと

- 問題データの形が変わった理由
- 出題順のランダム化（`questions` を直接シャッフル）
- ラジオボタンを毎回作り直さずに「使い回す」発想
- 3つのボタンの「押せる／押せない」を進行状況に合わせて管理する仕組み

---

# ①　問題データの形が変わった

演習⑤では、こういう形だった。

```python
questions = [
    ("日本でいちばん高い山は？", "富士山"),
    ("日本の国花は？", "桜"),
    ("日本の首都は？", "東京")
]
```

`(問題文, 正解)` の2つ組。今回は三択にするので、不正解の選択肢も持たせる必要がある。

```python
questions = [
    ("日本でいちばん高い山は？", "富士山", ["北岳", "奥穂高岳"]),
    ("日本の国花は？", "桜", ["菊", "藤"]),
    ("日本の首都は？", "東京", ["大阪", "京都"]),
]
```

`(問題文, 正解, [不正解のリスト])` という3つ組になった。
タプルの中にリストを入れられる、というのは演習⑤（クイズ①）ではやらなかった形だけど、
「タプルはいろんな種類のデータをひとまとめにできる箱」ということを思い出せば自然な拡張。

---

# ②　🆕 出題番号のランダム化：`questions` を直接シャッフル

## やりたいこと

問題を出す順番をランダムにしたい。

## 考え方

一番シンプルな方法は、`questions` リスト自体をシャッフルしてしまうこと。

```python
random.shuffle(questions)   # questionsの中身の並び順が直接変わる
```

`current_question` はこれまで通り「`questions` の何番目か」を表す番号のまま。
`questions` 自体の並びがランダムになっているので、`current_question` を
0, 1, 2 と増やしていくだけで、自然にランダムな順で出題される。

```python
question_text = questions[current_question][0]
correct_answer = questions[current_question][1]
wrong_answers = questions[current_question][2]
```

演習④・⑤で書いていた `questions[current_question][0]` と同じやり方。
`[0]` `[1]` `[2]` で、タプルの中身を1つずつ順番に取り出している。

#### 🆕 新しい道具：`random.shuffle()`

演習①で使った `random.choice()` は「1個選ぶ」命令だったけど、
`random.shuffle()` は**リストの中身の並び順をシャッフルする**命令。

```python
numbers = [1, 2, 3]
random.shuffle(numbers)
print(numbers)   # [3, 1, 2] のように、numbers自体の順番が変わる（新しいリストは作らない）
```

> 💡 `random.choice()` は「1つ取り出す」、`random.shuffle()` は「並び替える」。似ているようで役割が違う。

> 💡 補足：`questions` の中身の順番を別のリスト（例えば `quiz_order`）で管理する、という書き方もできる。
> 元のデータを書き換えずに済むという利点はあるけど、今回のアプリではどちらで書いても動きは同じ。
> 今回は**シンプルに書ける方**を選んだ。

---

# ③　🆕 選択肢のランダム化とウィジェットの「使い回し」

## やりたいこと

正解1つ・不正解2つを混ぜて、毎回違う順番でラジオボタンに表示したい。

## 選択肢を混ぜてシャッフルする

```python
choices = wrong_answers + [correct_answer]   # リストを結合して3つの選択肢にする
random.shuffle(choices)                       # 並び順をシャッフル
```

`wrong_answers` はリスト、`correct_answer` は文字列なので、そのままでは足せない。
`[correct_answer]` と1個だけのリストにしてから `+` で結合している。

## 🆕 ラジオボタンを「使い回す」

演習④・⑤までは、ウィジェットは画面を作るときに1回だけ作って、
その後は `.config()` で文字や色を変えるだけだった。

今回もその考え方をそのまま使う。**問題ごとにラジオボタンを作り直すのではなく、
最初に3つだけ作っておいて、問題が変わるたびに中身（表示文字と値）だけ差し替える。**

```python
# 画面づくりの部分：最初に3つだけ作っておく
radio_buttons = []
for i in range(3):
    rb = tk.Radiobutton(radio_frame, text="", variable=selected, value="", font=("Arial", 12))
    rb.pack(anchor="w")
    radio_buttons.append(rb)
```

```python
# show_question()の中：中身だけ差し替える
for rb, choice in zip(radio_buttons, choices):
    rb.config(text=choice, value=choice, state="normal")
```

#### 🆕 新しい道具：`zip()`

`zip()` は、**2つのリストを同じ順番でペアにして、同時に取り出す**命令。

```python
radio_buttons = [rb1, rb2, rb3]
choices = ["東京", "大阪", "京都"]

for rb, choice in zip(radio_buttons, choices):
    print(rb, choice)
# (rb1, "東京) → (rb2, "大阪") → (rb3, "京都") の順でペアになる
```

`radio_buttons` の1個目と `choices` の1個目、2個目同士、3個目同士…とペアにして
同時にループを回せるので、「ラジオボタンと選択肢を対応させながら書き換える」処理が1つの`for`で書ける。

> 💡 もし `zip()` を使わずに書こうとすると、`for i in range(3):` として
> `radio_buttons[i]` と `choices[i]` を毎回書く必要があって、コードが少し読みにくくなる。

---

# ④　答え合わせ・次の問題・リトライの流れ

## `check_answer()`：答え合わせ

```python
def check_answer():
    global current_question, score

    user_answer = selected.get()

    if user_answer == "":
        result_label.config(text="選択肢を選んでね！", fg="orange")
        return
    ...

    check_button.config(state="disabled")
    for rb in radio_buttons:
        rb.config(state="disabled")
    next_button.config(state="normal")
```

`selected.get()` で、今チェックされているラジオボタンの `value` を取得する。
何も選ばれていなければ空文字が返ってくるので、先にそれをチェックして、
選んでいなければ答え合わせをせずに `return` で処理を抜ける（これは演習④・⑤にはなかった、
仁礼くん自身が入力チェックを自主的にやっていたのと同じ発想）。

答え合わせが終わったら、ラジオボタンと「答え合わせ」ボタンを `disabled` にして、
1問につき1回しか答えられないようにしている。そして最後の1行で `next_button` を
`normal` にして、「次の問題」ボタンが**ここで初めて**押せるようになる。

## `next_question()`：次の問題へ

`current_question` を1つ増やして、`questions` の範囲内なら次の問題を表示。
範囲を超えたら終了処理（全部のボタンを`disabled`にして、正解数を表示し、
`retry_button` だけ `normal` にする）。このあたりの流れは演習⑤とほぼ同じ。

## `retry_quiz()`：🆕 最初からやり直す

```python
def retry_quiz():
    global current_question, score

    current_question = 0
    score = 0
    random.shuffle(questions)

    check_button.config(state="normal")
    retry_button.config(state="disabled")

    show_question()
```

やっていることは「①〜③で作った状態を、最初の状態に戻す」だけ。

- `current_question` と `score` を0に戻す
- `questions` をもう一度シャッフルする（＝出題順が毎回変わる）
- `check_button` を `normal` に、`retry_button` は自分自身を `disabled` に戻す
- `show_question()` を呼んで最初の問題を表示する（`show_question()` の中で
  ラジオボタンが `normal`、`next_button` が `disabled` に戻る）

「リトライ」という新しい動きに見えるけど、中身は**すでにある変数をもう一度初期化しているだけ**。
新しい仕組みは何も使っていない、というのがポイント。

---

# ⑤　ボタンの状態を操作する


- 答え合わせをする**前**は「次の問題」ボタンが押せないようにする
- クイズが全て終わった状態で「リトライ」ボタンが押せるようにする

ボタンが「押せる／押せない」を、**今どういう状況か**に合わせて切り替える必要がある。

## 考え方：ボタンの状態を、進行状況に合わせて管理する

演習④・⑤で、答え合わせ後に `check_button` を `disabled` にする、というのはやっていた。
今回はこれをさらに広げて、**3つのボタンそれぞれについて「いつ押せて、いつ押せないか」を
最初から最後まで一貫して管理する**。

| ボタン | 押せるタイミング | 押せないタイミング |
|---|---|---|
| 答え合わせ | 新しい問題が出た直後 | 答え合わせした直後〜次の問題が出るまで |
| 次の問題 | 答え合わせした直後 | 新しい問題が出た直後〜答え合わせするまで |
| リトライ | 全問終了した直後 | それ以外すべて（クイズの最中はずっと） |

## 実装のポイント：ボタンを作る時点で最初から `disabled`

```python
next_button = tk.Button(root, text="次の問題", font=("Arial", 12), command=next_question, state="disabled")
retry_button = tk.Button(root, text="リトライ", font=("Arial", 12), command=retry_quiz, state="disabled")
```

アプリを起動した直後は「まだ何も答えていない」「まだ1問も終わっていない」状態なので、
`next_button` と `retry_button` は最初から `disabled` にしておく。
（`check_button` は最初から答えられる必要があるので `normal` のまま）

## 実装のポイント：状態が変わるたびに、関係するボタンだけ書き換える

- `check_answer()`（答え合わせ完了）→ `next_button` を `normal` に
- `show_question()`（新しい問題を表示）→ `next_button` を `disabled` に**戻す**
- `next_question()`（全問終了）→ `retry_button` を `normal` に
- `retry_quiz()`（リトライ実行）→ `retry_button` を自分で `disabled` に**戻す**

「押せるようにする」だけでなく、「用が済んだらまた押せないように戻す」の
**両方をセットで書く**のがポイント。片方だけ書くと、一度押せるようになったボタンが
ずっと押せたままになってしまう。

> 💡 これは新しい道具というより、`state="normal"` / `state="disabled"` という
> すでに知っている道具を、「アプリの状態（今どこにいるか）ときちんと対応させる」という
> 設計の話。今回のように機能が増えてボタンの数が増えるほど、この管理が大事になってくる。

---

# ⑥　おまけ：ラジオボタンが最初から選択済みに見える件

実行してみると、ラジオボタンが3つとも最初からチェックされているように見える。
一見バグに見えるけど、これは**コードの間違いではなく、見た目だけの話**。

## 確かめ方

何もクリックせずに「答え合わせ」ボタンを押してみると、
「選択肢を選んでね！」ときちんと表示される。

```python
user_answer = selected.get()

if user_answer == "":
    result_label.config(text="選択肢を選んでね！", fg="orange")
    return
```

これが表示されるということは、`selected.get()` は3つとも未選択の状態を
正しく `""` として返せている、つまり**プログラムの中身（ロジック）は正しく動いている**ということ。

## 結論

見た目が選択済みっぽく見えるのは、**このWindows環境でのTkinterのラジオボタンが、
「未選択」の状態をこういうデザイン（小さい黒丸入りの円）で描画する**、というだけの話。
見慣れているチェックの入り方（空の白い丸）と違うので、選択済みに錯覚してしまう。

> 💡 これは大事な教訓：「見た目がおかしい＝コードが間違っている」とは限らない。
> `selected.get()` の中身を実際に確認する（今回は「答え合わせ」ボタンの反応で間接的に確認した）ことで、
> 「ロジックは合っている／見た目だけの話」と切り分けられる。
> 憶測でコードを直す前に、まず**変数の中身を確認する**クセをつけると、無駄な修正を減らせる。

---

## 今日のまとめ

| 道具・考え方 | やっていること |
|---|---|
| `random.shuffle()` | リストの並び順をランダムに変える（`questions` を直接シャッフルして出題順を変える） |
| ウィジェットの使い回し | 部品を毎回作り直さず、`.config()`で中身だけ差し替える |
| `zip()` | 2つのリストをペアにして同時にループする |
| ボタンのstate管理 | 「押せるようにする」だけでなく「用が済んだら戻す」も忘れずセットで書く |
| 見た目 vs ロジック | 「おかしく見える」＝「コードが間違っている」とは限らない。まず変数の中身を確認する |

**おつかれさま！ 次はToDoアプリだよ！**
