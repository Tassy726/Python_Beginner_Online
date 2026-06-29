import tkinter as tk

root = tk.Tk()
root.title("カンタン計算アプリ")
root.geometry("350x280")
root.resizable(False, False)

def calculate():
    try:
        num1 = Entyr1.get()
        num2 = Entyr2.get()
        result = float(num1) + float(num2)
        answer_label.config(text=f"答え：{result}")
    except ValueError:
        answer_label.config(text="エラー：数字を入力してください")


title_label = tk.Label(root, text="カンタン計算アプリ", font=("Arial", 16))
title_label.pack(pady=10)

label1 = tk.Label(root, text="1つ目の数字")
label1.pack()

Entyr1 = tk.Entry(root, width=20)
Entyr1.pack(pady=5)

label2 = tk.Label(root, text="2つ目の数字")
label2.pack()

Entyr2 = tk.Entry(root, width=20)
Entyr2.pack(pady=5)

button = tk.Button(root, text="計算する", command=calculate)
button.pack(pady=10)

answer_label = tk.Label(root, text="答え：", font=("Arial", 14))
answer_label.pack(pady=10)


root.mainloop()