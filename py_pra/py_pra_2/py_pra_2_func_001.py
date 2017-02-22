# 2016.4.24
# Python
# thisProgram_Have_Meaning_1 (tPHM_1)
# 意味があるプログラム(決してごみではない)
# func_1 : 入力した何らかの値に対して０～９のいずれかを返す
# func_2 : 引数で０～９をもらい、それぞれで処理する（例：占い）

# -->> for <<--Great_fantastic_wnderful_marvelous_excellent
# Pythonのfor文は素晴らしい。
# 繰り返したい回数を指定するのに、そのまま文字列を持ってこれる

def func_1():
    data = input()
    data_2 = 0 # 宣言
    for i in data:
        data_2 += ord(i)
        #print(ord(i))

    result = data_2 % 10 # ０～９を作る
    #print(result)
    return result

def func_2(value):
    if value == 1:
        print('I like playing game.(Now:splatoon)')
    elif value == 2:
        print('I can fly.')
    elif value == 3:
        print('I\'m reading.')
    elif value == 4:
        print('I\'m sleeping.')
    elif value == 5:
        print('I like watching movies.')
    elif value == 6:
        print('I like studying.')
    elif value == 7:
        print('I\'m studying Python.')
    elif value == 8:
        print('I want to study English.')
    elif value == 9:
        print('I want to study math.')
    elif value == 10:
        print('I enjoy life.')
    else:
        print('It happens.')

value = func_1()
func_2(value)
