import tkinter as tk

# 問題と答え
questions = [
    ("日本でいちばん高い山は？", "富士山"),
    ("1 + 1 はいくつ？", "2"),
    ("日本の首都は？", "東京")
]

# 状態管理
current_question = 0
score = 0

# 答えをチェック
def check_answer():
    global current_question, score

    user_answer = entry.get()
    correct_answer = questions[current_question][1]

    if user_answer == correct_answer:
        score += 1
        result_label.config(text="正解！", fg="blue")
    else:
        result_label.config(text=f"不正解！（答え：{correct_answer}）", fg="red")

# 次の問題へ
def next_question():
    global current_question

    current_question += 1

    if current_question < len(questions):
        show_question()
        entry.delete(0, tk.END)
        result_label.config(text="")
    else:
        # 終了
        question_label.config(text="クイズ終了！")
        result_label.config(text=f"{len(questions)}問中 {score}問正解！", fg="green")
        check_button.config(state="disabled")
        next_button.config(state="disabled")

# 問題表示
def show_question():
    question_label.config(text=questions[current_question][0])

# メイン画面
root = tk.Tk()
root.title("ミニクイズアプリ")
root.geometry("450x300")
root.resizable(False, False)

# タイトル
title_label = tk.Label(root, text="ミニクイズアプリ", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# 問題表示
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
question_label.pack(pady=10)

# 入力欄
entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.pack(pady=10)

# 判定ボタン
check_button = tk.Button(root, text="答え合わせ", font=("Arial", 12), command=check_answer)
check_button.pack(pady=5)

# 次へボタン
next_button = tk.Button(root, text="次の問題", font=("Arial", 12), command=next_question)
next_button.pack(pady=5)

# 結果表示
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# 最初の問題を表示
show_question()

# 起動
root.mainloop()