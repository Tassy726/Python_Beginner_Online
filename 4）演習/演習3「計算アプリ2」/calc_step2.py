# 演習③ カンタン計算アプリ２（四則演算対応バージョン）

import tkinter as tk

# 計算する関数
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = sel.get()              # 選ばれた演算子を取り出す

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2

        result_label.config(text=f"答え：{result}", fg="black")

    except ValueError:
        result_label.config(text="エラー：数字を入力してください", fg="red")
    except ZeroDivisionError:
        result_label.config(text="エラー：0で割ることはできません", fg="red")


# メインウィンドウ
root = tk.Tk()
root.title("カンタン計算アプリ２")
root.geometry("350x320")
root.resizable(False, False)

# タイトル
title_label = tk.Label(root, text="カンタン計算アプリ２", font=("Arial", 16))
title_label.pack(pady=10)

# 1つ目の入力欄
label1 = tk.Label(root, text="1つ目の数字", font=("Arial", 12))
label1.pack()
entry1 = tk.Entry(root, width=20, font=("Arial", 12))
entry1.pack(pady=5)

# 演算子を記憶する変数（StringVar）
sel = tk.StringVar()
sel.set("+")                        # 起動時は「＋」を選んだ状態にする

# ラジオボタンをFrameの中で横並びに配置
radio_frame = tk.Frame(root)
radio_frame.pack(pady=8)

rb_add = tk.Radiobutton(radio_frame, text="＋", variable=sel, value="+", font=("Arial", 14))
rb_sub = tk.Radiobutton(radio_frame, text="－", variable=sel, value="-", font=("Arial", 14))
rb_mul = tk.Radiobutton(radio_frame, text="×", variable=sel, value="*", font=("Arial", 14))
rb_div = tk.Radiobutton(radio_frame, text="÷", variable=sel, value="/", font=("Arial", 14))

rb_add.pack(side="left", padx=6)
rb_sub.pack(side="left", padx=6)
rb_mul.pack(side="left", padx=6)
rb_div.pack(side="left", padx=6)

# 2つ目の入力欄
label2 = tk.Label(root, text="2つ目の数字", font=("Arial", 12))
label2.pack()
entry2 = tk.Entry(root, width=20, font=("Arial", 12))
entry2.pack(pady=5)

# 計算ボタン
calc_button = tk.Button(root, text="計算する", font=("Arial", 14), command=calculate)
calc_button.pack(pady=10)

# 結果表示ラベル
result_label = tk.Label(root, text="答え：", font=("Arial", 14))
result_label.pack(pady=5)

# アプリ起動
root.mainloop()