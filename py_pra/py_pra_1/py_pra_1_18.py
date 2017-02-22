# 2016.4.23
# Python
# File_read
# File_write

for i in range(3):
    f = open("py_pra_1.txt","r")    # encoding="utf-8"
    s = f.read()
    f.close()
    print('1')
    print(s)# s = "aaa"
    f = open("py_pra_1.txt","w")
    f.write(s)
    f.close()
    f = open("py_pra_1.txt","r+")
    s = f.read()
    f.write(s)
    #s = f.read()
    f.close()
    print('2')
    print(s)

