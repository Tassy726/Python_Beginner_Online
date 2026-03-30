import tkinter as tk
import random

# おみくじを引く関数
def draw_fortune():
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    result = random.choice(fortunes)
    result_label.config(text=f"結果：{result}")

# メインウィンドウ作成
root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("350x250")

# タイトル
title_label = tk.Label(root, text="おみくじアプリ", font=("Arial", 16))
title_label.pack(pady=10)

# 説明
message_label = tk.Label(root, text="ボタンを押して、おみくじを引こう！", font=("Arial", 12))
message_label.pack(pady=10)

# おみくじボタン
draw_button = tk.Button(root, text="おみくじを引く", font=("Arial", 14), command=draw_fortune)
draw_button.pack(pady=15)

# 結果表示ラベル
result_label = tk.Label(root, text="結果：？？？", font=("Arial", 18))
result_label.pack(pady=20)

# アプリ起動
root.mainloop()