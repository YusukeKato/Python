import sys
# 設定
print("石の数は？")
isi = input(">>>")
isi = int(isi)
print("一度にとれる石の数は？")
isiMax = input(">>>")
isiMax = int(isiMax)
if(isi < 1 or isiMax < 1):
    print("足りない")
    sys.exit()
# ゲーム本体
turn = 1
x = r = 0
flag = True
while isi != 0:
    if(flag):
        flag = False
        x = (isi - 1) % (isiMax + 1)
        if(x == 0):
            x = 1
        print("私は %d 個の石をとります." %x)
    else:
        flag = True
        flag2 = True
        while flag2:
            print("何個とりますか？")
            x = input(">>>")
            x = int(x)
            if(not(x <= 0 or x > isi or x > isiMax)):
                flag2 = False
    isi -= x
    print("残りは %d 個です." %isi)
if(flag):
    print("あなたの負け")
else:
    print("私の負け")
