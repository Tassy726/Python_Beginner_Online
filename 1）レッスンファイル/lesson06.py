# レッスン６：「おみくじのプログラム」

'''
「モジュール」
モジュールとは、Pythonで、特定の便利機能をファイルにまとめたもの。
似た働きをする関数の集合が「モジュール」ともいえる。
プログラムで必要な時に呼び出して使うことができる。
Pythonが格納されているフォルダに含まれている"Python Module Docs"で
モジュールの一覧を確認することができる。
'''

# モジュールの呼び出し方１：モジュールは、プログラムの一番先頭に"import モジュール名"で呼び出す
import random   # randomは乱数に関するモジュール


# モジュール名の呼び出し方２：長いモジュール名などに略称を付けたい場合は"as"を使う
import tkinter as Tk    #Tkはtkinterモジュールの略称として任意に名付けたもの


# モジュールの呼び出し方３："from モジュール名　import そのモジュール内の特定の関数"
from math import sqrt   # "math"は数学的計算に関するモジュール、"sqrt"は平方根を計算する関数


# おみくじのプログラム

import random   # random（乱数）モジュールの読み込み

result = random.randint(1, 4)   # １から４の整数で乱数を発生し、その値を変数に代入

if result == 1:     #if文を使って、表示させる「くじ」を決める
    print("大吉！")
elif result == 2:
    print("小吉")
elif result == 3:
    print("吉")
else:
    print("凶！")