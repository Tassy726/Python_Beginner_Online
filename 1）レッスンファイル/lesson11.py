# レッスン１１「tkinter② ボタンと関数」

'''
前回のレッスンで、ウィンドウ・ラベル・ボタンを画面に表示できるようになった。
でも、ボタンを押しても何も起きなかった。

今回は、ボタンに「関数」を結びつけて、
ボタンを押したら画面が変わるプログラムを作ろう！
'''


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 【ステップ１】ボタンに関数を割り当てる（command）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

'''
ボタンに「押したときに実行する関数」を設定するには、
tk.Button() の中に command=関数名 を追加する。

⚠ 注意：command=on_click であって command=on_click() ではない！
カッコ()を付けると「今すぐ実行」になってしまう。
command には「関数名だけ」を渡す。
'''

import tkinter as tk

root = tk.Tk()
root.title("command のテスト")
root.geometry("400x300")


# ボタンが押されたときに実行する関数
def on_click():
    print("ボタンが押されました！")     # ターミナルに表示される


# command=on_click で、ボタンとon_click関数を結びつける
btn = tk.Button(root, text="クリック", font=("Arial", 14), command=on_click)
btn.pack(pady=50)

root.mainloop()




# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 【ステップ２】画面の表示を変える（config）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

'''
ステップ１では、ボタンを押した結果がターミナルに表示された。
でも、アプリとしては「画面の中」で変化が見えた方がいい。

.config() を使うと、表示済みのウィジェットを後から変更できる。

【書き方】
　ウィジェット名.config(プロパティ=新しい値)
※ config()はconfigure()の略。どちらを使っても良い。

【例】
　lb.config(text="新しいテキスト")      ← ラベルの文字を変える
　lb.config(font=("Arial", 24))        ← ラベルのフォントを変える
　btn.config(text="押した！")           ← ボタンの文字を変える

ウィンドウ（root）の背景色を変えるには：
　root.configure(bg="色名")
'''

import tkinter as tk

root = tk.Tk()
root.title("config のテスト")
root.geometry("400x300")

lb = tk.Label(root, text="ここが変わるよ", font=("Arial", 18))
lb.pack(pady=30)


def on_click():
    lb.config(text="ボタンが押された！")    # ラベルの文字を変更
    root.configure(bg="lightgreen")         # 背景色を変更


btn = tk.Button(root, text="クリック", font=("Arial", 14), command=on_click)
btn.pack(pady=20)

root.mainloop()




# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 【ステップ３】応用：サイコロアプリ
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

'''
レッスン６で使った random モジュールと tkinter を組み合わせて、
ボタンを押すとサイコロを振れるアプリを作ってみよう！

使うもの：
・import random      ← 乱数（レッスン６）
・command=関数名     ← ボタンに関数を割り当てる（ステップ１）
・lb.config()        ← ラベルの文字を変える（ステップ２）
'''

import tkinter as tk
import random

root = tk.Tk()
root.title("サイコロアプリ")
root.geometry("400x300")

lb = tk.Label(root, text="？", font=("Arial", 80))
lb.pack(pady=30)


def roll_dice():
    result = random.randint(1, 6)       # 1〜6の乱数を出す
    lb.config(text=result)              # ラベルにサイコロの目を表示


btn = tk.Button(root, text="サイコロを振る", font=("Arial", 14), command=roll_dice)
btn.pack(pady=20)

root.mainloop()


# ── 発展チャレンジ ──
# サイコロの出た目によって背景色が変わるようにしてみよう！
# ヒント：roll_dice() の中で if文 を使って、
#         result の値に応じて root.configure(bg="色名") を変える



# 【今日のまとめ】
#
# ① command=関数名 → ボタンに関数を割り当てる（カッコは付けない！）
# ② .config()      → ウィジェットの見た目を後から変えられる
# ③ random + tkinter を組み合わせると「アプリっぽいもの」が作れる！
#

