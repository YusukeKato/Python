#2016.4.21
# python

def func_1():
    print(0x1ff)
    print(hex(1023))
    print(int("0x100",16))
    print(0b1100)
    print(bin(1023))
    print(int("0b1111111111",2))
    print(0o1777)
    print(oct(1023))
    print(int("0o1777",8))

def func_2():
    s = "abcdefgh"
    print(s.find("def"))
    print(s.rfind("ppp"))
    print(s.index("def"))
    # print(s.rindex("ppp")) # 正しい
    print(s.endswith("gh"))
    print(s.startswith("abc"))
    S = "abc def ghijk opq"
    S.split()
    print(S)
    " ".join(S)
    print(S)

def add_tax(astring):
    items = astring.split()
    price = int(items[1]) * 1.1
    items[1] = str(int(price))
    print(" ".join(items))

def func_3():
    s = "abcde"
    S = s.upper()
    print(S)
    s =  S.lower()
    print(s)
    print(s.ljust(4)) # 分からない

def func_4():
    a = "{} abcde".format("ttt")
    print(a)
    linkstr = '<a href = "{}">{}</a>'
    for i in[ 'http://python.org',
              'http://pypy.org',
              'http://jython.org',]:
        print(linkstr.format(i, i.replace('http://','')))
    b = "{0}{2}{1}".format('a','b','c')
    print(b)
    c = "{c1}{c2}{c3}".format(c1 = 'red',
                              c2 = 'blue',
                              c3 = 'yellow')
    print(c)

def func_5():
    a = [1,2,3,4,5,6,7,8,9]
    print(a[::2])
    a[3:5] = ['aaa','bbb','ccc']
    print(a)
    del a[5:]
    print(a)

def func_6():
    a = 1
    b = 2
    a,b = b,a
    print(a,b)
    


func_1()
func_2()
add_tax("Goods 1000 2016/4/21")
func_3()
func_4()
func_5()
func_6()









