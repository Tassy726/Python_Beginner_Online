import tkinter as tk
import random

# 問題データ（質問, 正解, 不正解の選択肢リスト）
questions = [
    ("日本でいちばん高い山は？", "富士山", ["北岳", "奥穂高岳"]),
    ("日本の国花は？", "桜", ["菊", "藤"]),
    ("日本の首都は？", "東京", ["大阪", "京都"]),
]

# 状態管理
current_question = 0
score = 0


# 答えをチェック
def check_answer():
    global current_question, score

    user_answer = selected.get()

    if user_answer == "":
        result_label.config(text="選択肢を選んでね！", fg="orange")
        return

    correct_answer = questions[current_question][1]

    if user_answer == correct_answer:
        score += 1
        result_label.config(text="正解！", fg="blue")
    else:
        result_label.config(text=f"不正解！（答え：{correct_answer}）", fg="red")

    check_button.config(state="disabled")
    for rb in radio_buttons:
        rb.config(state="disabled")
    next_button.config(state="normal")


# 次の問題へ
def next_question():
    global current_question

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        # 終了
        question_label.config(text="クイズ終了！")
        result_label.config(text=f"{len(questions)}問中 {score}問正解！", fg="green")
        for rb in radio_buttons:
            rb.config(state="disabled")
        check_button.config(state="disabled")
        next_button.config(state="disabled")
        retry_button.config(state="normal")


# 問題を表示する（選択肢の並び順もランダムにする）
def show_question():
    question_text = questions[current_question][0]
    correct_answer = questions[current_question][1]
    wrong_answers = questions[current_question][2]

    question_label.config(text=question_text)

    choices = wrong_answers + [correct_answer]
    random.shuffle(choices)

    for rb, choice in zip(radio_buttons, choices):
        rb.config(text=choice, value=choice, state="normal")
    selected.set("")  # 選択状態をリセット

    result_label.config(text="")
    check_button.config(state="normal")
    next_button.config(state="disabled")


# 最初からリトライする
def retry_quiz():
    global current_question, score

    current_question = 0
    score = 0
    random.shuffle(questions)

    check_button.config(state="normal")
    retry_button.config(state="disabled")

    show_question()


# メイン画面
root = tk.Tk()
root.title("ミニクイズアプリ２")
root.geometry("450x380")
root.resizable(False, False)

# タイトル
title_label = tk.Label(root, text="ミニクイズアプリ２", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# 問題表示
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
question_label.pack(pady=10)

# 選択状態を記憶する仕組み
selected = tk.StringVar()

# ラジオボタン（選択肢）を並べるミニウィンドウ
radio_frame = tk.Frame(root)
radio_frame.pack(pady=5)

radio_buttons = []
for i in range(3):
    rb = tk.Radiobutton(radio_frame, text="", variable=selected, value="", font=("Arial", 12))
    rb.pack(anchor="w")
    radio_buttons.append(rb)

# 判定ボタン
check_button = tk.Button(root, text="答え合わせ", font=("Arial", 12), command=check_answer)
check_button.pack(pady=5)

# 次へボタン（最初は押せない。答え合わせが終わってから押せるようにする）
next_button = tk.Button(root, text="次の問題", font=("Arial", 12), command=next_question, state="disabled")
next_button.pack(pady=5)

# リトライボタン（最初は押せない。全問終了してから押せるようにする）
retry_button = tk.Button(root, text="リトライ", font=("Arial", 12), command=retry_quiz, state="disabled")
retry_button.pack(pady=5)

# 結果表示
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# 問題の順番をシャッフルしてから、最初の問題を表示
random.shuffle(questions)
show_question()

# 起動
root.mainloop()
