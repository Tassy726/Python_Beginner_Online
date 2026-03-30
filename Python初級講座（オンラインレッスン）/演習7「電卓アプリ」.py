import tkinter as tk
from tkinter import messagebox

# ボタンが押されたとき、表示欄に文字を追加する
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# 計算を実行する
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("計算エラー", "0で割ることはできません。")
        clear()
    except Exception:
        messagebox.showerror("入力エラー", "正しい式を入力してください。")
        clear()

# 表示欄をクリアする
def clear():
    entry.delete(0, tk.END)

# メインウィンドウ作成
root = tk.Tk()
root.title("電卓アプリ")
root.geometry("320x420")
root.resizable(False, False)

# 表示欄
entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# ボタンの情報
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# ボタンを配置
for row_index, row_values in enumerate(buttons, start=1):
    for col_index, text in enumerate(row_values):
        if text == "=":
            btn = tk.Button(
                root,
                text=text,
                font=("Arial", 18),
                width=5,
                height=2,
                command=calculate
            )
        elif text == "C":
            btn = tk.Button(
                root,
                text=text,
                font=("Arial", 18),
                width=5,
                height=2,
                command=clear
            )
        else:
            btn = tk.Button(
                root,
                text=text,
                font=("Arial", 18),
                width=5,
                height=2,
                command=lambda value=text: click_button(value)
            )

        btn.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

# 行・列のサイズ調整
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()