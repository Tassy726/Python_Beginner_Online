# レッスン１０「tkinter」

'''
「tkinter」とは、Pythonでデスクトップアプリ（ウィンドウやボタンなどのGUI）を作るための標準ライブラリ。
・追加インストール不要（Pythonに最初から付属）
・ウィンドウ、ボタン、ラベル、入力欄などを簡単に作れる
・小規模なツールや学習用アプリ作成に向いている
'''

# tkinterの最小構成
import tkinter as tk    # tkinterライブラリを読み込む（tkという略称にする）
root = tk.Tk()          # アプリのメインウィンドウ（土台）を作成し、変数rootに代入    
  # ここに、アプリのパーツ（ボタン、テキストボックス等）を入れる 
root.mainloop()         # アプリを表示し、ユーザーの操作を待ち続ける「イベントループ」を開始


# tkinterのプロパティ（属性）

root.title("タイトル")      #ウインドウのタイトルバーに表示させる「タイトル」

root.geometry("600x300")    #ウインドウのサイズ設定。文字列で"ヨコxタテ"のピクセルで指定

root.configure(bg="skyblue")    #ウインドウの背景色

# tkinterのウィジェット

 # ラベル （文字列）
lb = tk.Label(root, text="ラベル", font=("Arial", 18))  # lbは任意の変数、Label関数の引数で、表示させるウインドウ（root）、テキスト、フォント、フォントサイズを設定

  # ボタン
btn = tk.Button(root, text="ボタン", font=("Arial", 12))  

 # 1行のテキストボックス
ent = tk.Entry(root, width=30)    # 引数はroot、幅

 # 複数行のテキストボックス
txt = tk.Text(root, width=40, height=5)    # 引数はroot、幅、高さ

 # チェックボックス
var = tk.BooleanVar()   # チェック状態を保持する変数
check = tk.Checkbutton(root, text="同意します", variable=var) # 引数はroot、テキスト、チェック状態を入れる変数

# 他にもウィジェットには、ラジオボタン、ドロップダウンリスト、画像の描画領域などたくさんあります！


# ウィジェットの配置方法

 # 単純に上から順番に配置。例：配置するウィジェットの変数名.pack()
lb.pack()

 # 位置を指定して配置
lb.place(x=50, y=80)    #ウインドウの左上を起点（x=0,y=0）に座標で指定




