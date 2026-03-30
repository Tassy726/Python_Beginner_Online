import tkinter as tk
import random
import os

# おみくじ処理
def draw_fortune():
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    result = random.choice(fortunes)

    # 色変化
    if result == "大吉":
        color = "gold"
    elif result == "凶":
        color = "blue"
    else:
        color = "red"

    result_label.config(text=result, fg=color)

# パス取得
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "omikuji.png")

# ウィンドウ
root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("640x480")
root.resizable(False, False)

# 背景画像
bg_image = tk.PhotoImage(file=image_path)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, width=640, height=480)

# -------------------------
# 右側UI配置（ここが重要）
# -------------------------

# タイトル
title_label = tk.Label(
    root,
    text="おみくじアプリ",
    font=("Arial", 24, "bold"),
    fg="black"
)
title_label.place(x=520, y=60, anchor="center")

# 説明
message_label = tk.Label(
    root,
    text="ボタンを押して\nおみくじを引こう！",
    font=("Arial", 14),
    justify="center"
)
message_label.place(x=520, y=130, anchor="center")

# ボタン
draw_button = tk.Button(
    root,
    text="おみくじを引く",
    font=("Arial", 16),
    command=draw_fortune
)
draw_button.place(x=520, y=220, width=180, height=45, anchor="center")

# 結果表示
result_label = tk.Label(
    root,
    text="？？？",
    font=("Arial", 32, "bold")
)
result_label.place(x=520, y=330, anchor="center")

# 起動
root.mainloop()