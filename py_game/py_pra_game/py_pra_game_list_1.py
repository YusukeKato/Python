# 2016.4.26
# Python

# game_1
# listを用いたゲーム
# C言語でもやったやつ

# 注意：printの末尾に自動的に改行が入る

field = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]
x = 3
y = 2
field[y][x] = 1 # キャラクタ初期位置

# fieldの表示
def field_print():
    for j in range(5):
        print("") # 改行のため
        for i in range(7):
            print(field[j][i],end="") # end=""は自動での改行を防ぐため

# キャラクタの移動（１のこと）
def char_moution(x,y):
    w = s = d = a = 0 # 初期化
    field[y][x] = 0 # 元の位置を０にする
    print("\n入力：")
    mou = input()
    if(mou == 'w'):
        if(y > 0):
            y -= 1
            w = 1 # 関数外に伝えるために必要
    elif(mou == 's'):
        if(y < 4):
            y += 1
            s = 1 # もっと良い方法を考える
    elif(mou == 'd'):
        if(x < 6):
            x += 1
            d = 1 # 関数外に伝えるために必要
    elif(mou == 'a'):
        if(x > 0):
            x -= 1
            a = 1 # もっと良い方法を考える
    elif(mou == 'q'):
        return 0
    else:
        return 5

    field[y][x] = 1 # キャラクタの移動

    # returnで返す
    if(w == 1):
        return 1
    elif(s == 1):
        return 2
    elif(d == 1):
        return 3
    elif(a == 1):
        return 4
    else:
        return 5

#main_Loop
mout = 5 # 条件判別
while True:
    field_print()
    mout = char_moution(x,y)
    if(mout == 0):
        break
    # ローカル変数の問題
    # 関数内の変数をどう扱うか考える必要あり
    elif(mout == 1):
        y -= 1
    elif(mout == 2):
        y += 1
    elif(mout == 3):
        x += 1
    elif(mout == 4):
        x -= 1
    elif(mout == 5):
        print("miss")
