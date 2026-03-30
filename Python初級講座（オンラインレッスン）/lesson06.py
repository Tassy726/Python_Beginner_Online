# レッスン６：「おみくじのプログラム」

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