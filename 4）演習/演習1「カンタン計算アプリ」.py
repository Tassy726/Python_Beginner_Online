import tkinter as tk
from tkinter import messagebox

# 計算する関数
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"答え：{result}")
    except ValueError:
        messagebox.showerror("入力エラー", "数字を入力してください。")

# メインウィンドウ作成
root = tk.Tk()
root.title("カンタン計算アプリ")
root.geometry("350x250")

# タイトル
title_label = tk.Label(root, text="カンタン計算アプリ", font=("Arial", 16))
title_label.pack(pady=10)

# 1つ目の入力欄
label1 = tk.Label(root, text="1つ目の数字")
label1.pack()
entry1 = tk.Entry(root, width=20)
entry1.pack(pady=5)

# 2つ目の入力欄
label2 = tk.Label(root, text="2つ目の数字")
label2.pack()
entry2 = tk.Entry(root, width=20)
entry2.pack(pady=5)

# 計算ボタン
calc_button = tk.Button(root, text="計算する", command=calculate)
calc_button.pack(pady=10)

# 結果表示ラベル
result_label = tk.Label(root, text="答え：", font=("Arial", 14))
result_label.pack(pady=10)

# アプリ起動
root.mainloop()