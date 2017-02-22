# 2016.4.21
# Python

# if,elif,else
# input() 入力
def func_1():
    a = 0
    b = input() # input_number
    if a == 0:
        a = 1
    if a == 1:
        a = 2
    if a == 2:
        if b == 1:
            b = 10
        elif b == 2:
            b = 20
        else :
            b = 100
    print(a)
    print(b)

# == 比較
def func_2():
    s = "abcdefghi"
    print(s == "abcdefghi")
    a = [1,2,3]
    print(a == [1,2,3])
    if "def" in s:
        print("I found def")

# for,while
def func_3():
    for i in range(10,20):  # 10 - 19
        print(i)
    for j in range(0,10,2):
        print(j)
    c = 0
    while True: # mugen_Loop
        c += 1
        print(c)
        if c > 10:
            break

# int <--> str
# list && tuple
def func_4():
    num = 1
    char = "1"
    print(num == char)
    print(num == int(char))
    print(str(num) == char)
    print([1,2,3] == (1,2,3))
    

func_1()
func_2()
func_3()
func_4()
