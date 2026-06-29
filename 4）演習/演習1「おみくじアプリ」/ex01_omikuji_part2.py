# 演習① おみくじアプリ ── パート2「背景画像つきリッチ版」

import tkinter as tk
import random
import os                                                   # 🆕 ファイルパスを扱うモジュール

# おみくじを引く関数
def draw_fortune():
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    result = random.choice(fortunes)
    result_label.config(text=result)

# 🆕 画像ファイルのパスを組み立てる（このプログラムと同じフォルダにある画像を指す）
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "omikuji_BG.png")

# メインウィンドウ
root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("640x480")
root.resizable(False, False)


# 🆕 背景画像を読み込んでウィンドウ全体に配置
bg_image = tk.PhotoImage(file=image_path)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, width=640, height=480)

# ── 部品（ウィジェット）── 画面右半分に place() で配置
# 🆕 anchor="center" で、指定した座標が部品の「中心」になる

title_label = tk.Label(root, text="おみくじアプリ", font=("Arial", 24, "bold"))
title_label.place(x=520, y=60, anchor="center")

message_label = tk.Label(
    root,
    text="ボタンを押して\nおみくじを引こう！",
    font=("Arial", 14),
    justify="center"
)
message_label.place(x=520, y=140, anchor="center")

draw_button = tk.Button(
    root,
    text="おみくじを引く",
    font=("Arial", 16),
    command=draw_fortune
)
draw_button.place(x=520, y=230, width=180, height=45, anchor="center")

result_label = tk.Label(root, text="？？？", font=("Arial", 36, "bold"))
result_label.place(x=520, y=340, anchor="center")

# 起動
root.mainloop()
