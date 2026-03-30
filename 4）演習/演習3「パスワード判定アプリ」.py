import tkinter as tk

is_visible = False

# パスワード判定
def check_password():
    password = entry.get()

    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True

    # 判定
    if len(password) < 6:
        result = "NG：6文字以上にしてください"
        color = "red"
    elif has_lower and has_upper and has_digit and has_symbol:
        result = "強いパスワードです！"
        color = "green"
    else:
        result = "もう少し強くしましょう"
        color = "orange"

    result_label.config(text=result, fg=color)

# 表示切替
def toggle_password():
    global is_visible

    if is_visible:
        entry.config(show="*")
        toggle_button.config(text="表示")
        is_visible = False
    else:
        entry.config(show="")
        toggle_button.config(text="非表示")
        is_visible = True

# 画面
root = tk.Tk()
root.title("パスワード判定アプリ")
root.geometry("420x300")
root.resizable(False, False)

title_label = tk.Label(root, text="パスワード判定アプリ", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

message_label = tk.Label(root, text="パスワードを入力してください", font=("Arial", 12))
message_label.pack()

entry = tk.Entry(root, width=25, font=("Arial", 14), show="*")
entry.pack(pady=5)

toggle_button = tk.Button(root, text="表示", command=toggle_password)
toggle_button.pack()

check_button = tk.Button(root, text="判定する", font=("Arial", 14), command=check_password)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()