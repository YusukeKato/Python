# 2016.4.25
# Python

# ディクショナリを扱う
# 順番を持たない

dic = {"001":"study",
       "002":"music",
       "003":"reading",
       "004":"running",
       "005":"play_game"}

print(dic)

print("値の書き換え")
for d in dic:   # d:key一つ dic:key
    print("入力",d,"：")
    dic[d] = input()

print(dic)

print("keyの追加")
print("入力006:")
dic['006'] = input()

print(dic)

print("keyの削除")
print("入力001:")
del dic['001']

print(dic)



