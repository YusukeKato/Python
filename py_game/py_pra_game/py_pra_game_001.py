import random

dic = {"a":"グー", "b":"チョキ", "c":"パー"}

user = input("> ")
user = user.lower()

try:
    user2 = dic[user]
    plist = ["a", "b", "c"]
    com = dic[random.choice(plist)]

    win = "勝ち"
    lose = "負け"
    draw = "引き分け"

    if user2 == com:
        print(draw)
    elif user2 == "グー":
        if com == "パー":
            print(lose)
        elif com == "チョキ":
            print(win)
    elif user2 == "パー":
        if com == "グー":
            print(win)
        elif com == "チョキ":
            print(lose)
    elif user2 == "チョキ":
        if com == "グー":
            print(lose)
        elif com == "パー":
            print(win)
    print("あなた : %s" % user2)
    print("あいて : %s" % com)
except:
    print("error")
