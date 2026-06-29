# 演習① おみくじアプリ ── パート3「応用編：色分け＋確率操作」

import tkinter as tk
import random
import os

# おみくじを引く関数（応用①：色分けを追加）
def draw_fortune():
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]

    # 応用②：確率操作（大吉を出やすくしたい場合はリストに複数入れる）
    # fortunes = ["大吉", "大吉", "大吉", "中吉", "小吉", "吉", "末吉", "凶"]

    result = random.choice(fortunes)

    # 応用①：結果に応じて文字色を決める
    if result == "大吉":
        color = "gold"
    elif result == "凶":
        color = "blue"
    else:
        color = "red"

    result_label.config(text=result, fg=color)              # fg で文字色を指定

# 画像パスの組み立て
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "omikuji_BG.png")

# メインウィンドウ
root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("640x480")
root.resizable(False, False)

# 背景画像
bg_image = tk.PhotoImage(file=image_path)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, width=640, height=480)

# ── 部品（ウィジェット）──
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
