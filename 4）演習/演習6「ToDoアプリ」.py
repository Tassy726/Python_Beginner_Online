import tkinter as tk
from tkinter import messagebox

# 色設定
BG_COLOR = "#f0f8ff"
BUTTON_COLOR = "#add8e6"

# タスク追加
def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("入力エラー", "やることを入力してください。")
        return

    listbox.insert(tk.END, "☐ " + task)
    entry.delete(0, tk.END)

# 完了
def complete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("選択エラー", "項目を選んでください。")
        return

    index = selected[0]
    task = listbox.get(index)

    if task.startswith("☐ "):
        new_task = task.replace("☐ ", "☑ ", 1)
        listbox.delete(index)
        listbox.insert(index, new_task)

# 未完了に戻す
def uncomplete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("選択エラー", "項目を選んでください。")
        return

    index = selected[0]
    task = listbox.get(index)

    if task.startswith("☑ "):
        new_task = task.replace("☑ ", "☐ ", 1)
        listbox.delete(index)
        listbox.insert(index, new_task)

# 完了タスク削除
def delete_completed_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("選択エラー", "項目を選んでください。")
        return

    index = selected[0]
    task = listbox.get(index)

    if task.startswith("☑ "):
        listbox.delete(index)
    else:
        messagebox.showwarning("削除エラー", "完了したタスクだけ削除できます。")

# ウィンドウ
root = tk.Tk()
root.title("ToDoアプリ")
root.geometry("500x420")
root.resizable(False, False)

# 背景色
root.configure(bg=BG_COLOR)

# タイトル
title_label = tk.Label(
    root,
    text="ToDoアプリ",
    font=("Arial", 20, "bold"),
    bg=BG_COLOR,
    fg="#333"
)
title_label.pack(pady=10)

# 入力欄
entry = tk.Entry(root, width=28, font=("Arial", 14), bg="white")
entry.pack(pady=10)

# ボタン1行目
button_frame1 = tk.Frame(root, bg=BG_COLOR)
button_frame1.pack(pady=5)

add_button = tk.Button(
    button_frame1, text="追加", bg=BUTTON_COLOR,
    width=10, command=add_task
)
add_button.grid(row=0, column=0, padx=5)

complete_button = tk.Button(
    button_frame1, text="完了", bg=BUTTON_COLOR,
    width=10, command=complete_task
)
complete_button.grid(row=0, column=1, padx=5)

uncomplete_button = tk.Button(
    button_frame1, text="未完了に戻す", bg=BUTTON_COLOR,
    width=12, command=uncomplete_task
)
uncomplete_button.grid(row=0, column=2, padx=5)

# ボタン2行目
button_frame2 = tk.Frame(root, bg=BG_COLOR)
button_frame2.pack(pady=5)

delete_button = tk.Button(
    button_frame2,
    text="完了タスクを削除",
    bg="#ff9999",
    width=18,
    command=delete_completed_task
)
delete_button.grid(row=0, column=0, padx=5)

# リスト
listbox = tk.Listbox(
    root,
    width=40,
    height=12,
    font=("Arial", 14),
    bg="white",
    selectbackground="#87cefa"
)
listbox.pack(pady=15)

# 起動
root.mainloop()