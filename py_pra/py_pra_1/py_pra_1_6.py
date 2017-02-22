# 2016.4.20
# Python
# 荒ぶる関数 turbulent_function

# string + string
def func_1():
    nstr = "1234"
    result = nstr + "5678"
    print(result)

# string * int (value)(number)
def func_2():
    linestr = '-' * 20
    print(linestr)

# string -> int
def func_3():
    nstr = "1234"
    print(int(nstr) + 5678)

# int -> string
def func_4():
    nstr = "1234"
    print(nstr + str(5678))

# string of length
def func_5():
    word = "abcde"
    print(len(word))
    print(len("fghijklmn"))

# search_result : True or False
# replace
def func_6():
    address = "abcdefg"
    print("d" in address)
    print("h" in address)
    address.replace("f","fff")

# index
# ord(Character->CharacterCode)
# chr(CharacterCode->Character)
def func_7():
    digits = "1234"
    print(digits[2])
    print(ord(digits[2]))
    print(chr(52))

# a[-1] -> last
def func_8():
    a = [1,2,3,4,5]
    print(a[2])
    print(a[-1])

# slice(range_search)
def func_9():
    a = [1,2,3,4,5]
    print(a[1:3])
    print(a[3:4])
    print(a[2:])
    print(a[:3])
    print(a[2:100])

# list(+,*),delete
def func_10():
    a = [1,2,3]
    b = a + [100,101,102]
    print(b)
    print(a * 3)
    a[1] = 'a'
    print(a)
    del b[3]
    print(b)

# in_Operator
# object
def func_11():
    names = ["abc","def","hijkl","mn"]
    print("def" in names)
    print("opq" in names)
    print(names.index("hijkl"))

# max,min 
def func_12():
    data = [1,2,3,4,5]
    print(max(data))
    print(min(data))

# sort,reverse
def func_13():
    data = [2,5,4,3,1]
    data.sort()
    print(data)
    data.reverse()
    print(data)

# append(add_to)
def func_14():
    a = [1,2,3]
    a.append(100)
    print(a)
    a.append([200,300,400])
    print(a)
    a.extend([500,600,700])
    print(a)

# for
def func_15():
    board = [[0,1,2,3],
             [4,5,6,7],
             [8,9,10,11],
             [12,13,14,15]]
    for j in range(4):
        for i in range(4):
            print(board[j][i])

# dictionary
def func_16():
    d = {"100":"abc",
         "101":"def",
         "102":"ghijk"}
    print(d["101"])
    d["102"] = "lmnop"
    d["103"] = "qrstu"
    del d["101"]
    print(d.keys())

def func_17():
    t = (1,2,3,4,5)
    print(t[1])
    print(t[2:4])
    t2 = t + (100,200,300)
    print(t2)

# list <--> tuple
def func_18():
    t = (1,2,3)
    a = list(t)
    t2 = tuple(a)
    print(t2)

if __name__ == "__main__": # what is main?
    func_1()
    func_2()
    func_3()
    func_4()
    func_5()
    func_6()
    func_7()
    func_8()
    func_9()
    func_10()
    func_11()
    func_12()
    func_13()
    func_14()
    func_15()
    func_16()
    func_17()
    func_18()
    
    
    
        

