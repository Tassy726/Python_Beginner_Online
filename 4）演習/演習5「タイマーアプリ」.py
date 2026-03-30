import tkinter as tk

# 状態
remaining_seconds = 0
running = False

# タイマー更新
def update_timer():
    global remaining_seconds, running

    if running and remaining_seconds > 0:
        remaining_seconds -= 1

        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        timer_label.config(text=f"{minutes:02}:{seconds:02}")

        root.after(1000, update_timer)

    elif remaining_seconds == 0 and running:
        timer_label.config(text="00:00")
        result_label.config(text="タイムアップ！", fg="red")
        running = False

# スタート
def start_timer():
    global remaining_seconds, running

    if not running:
        try:
            minutes = int(entry_min.get())
            seconds = int(entry_sec.get())
            remaining_seconds = minutes * 60 + seconds

            if remaining_seconds > 0:
                running = True
                result_label.config(text="")
                update_timer()
        except:
            result_label.config(text="数字を入力してください", fg="red")

# ストップ
def stop_timer():
    global running
    running = False

# リセット
def reset_timer():
    global running, remaining_seconds
    running = False
    remaining_seconds = 0
    timer_label.config(text="00:00")
    result_label.config(text="")

# 画面
root = tk.Tk()
root.title("タイマーアプリ")
root.geometry("420x300")
root.resizable(False, False)

# タイトル
title_label = tk.Label(root, text="カウントダウンタイマー", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# 入力エリア
input_frame = tk.Frame(root)
input_frame.pack()

tk.Label(input_frame, text="分").grid(row=0, column=0)
entry_min = tk.Entry(input_frame, width=5)
entry_min.grid(row=0, column=1)

tk.Label(input_frame, text="秒").grid(row=0, column=2)
entry_sec = tk.Entry(input_frame, width=5)
entry_sec.grid(row=0, column=3)

# タイマー表示
timer_label = tk.Label(root, text="00:00", font=("Arial", 32, "bold"))
timer_label.pack(pady=20)

# ボタン
button_frame = tk.Frame(root)
button_frame.pack()

start_button = tk.Button(button_frame, text="スタート", command=start_timer)
start_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(button_frame, text="ストップ", command=stop_timer)
stop_button.grid(row=0, column=1, padx=10)

reset_button = tk.Button(button_frame, text="リセット", command=reset_timer)
reset_button.grid(row=0, column=2, padx=10)

# メッセージ
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()