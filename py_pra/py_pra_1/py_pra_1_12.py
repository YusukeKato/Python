# 2016.4.21
# python

# about_argument_function
def func_1(name,data,a = "ttt"):
    print("name",name)
    print(data[ord(name[0]) % len(data)])
    print(a)
    result = name + data[ord(name[0]) % len(data)]
    return result

data_1 = ["abc","def","ghijk"]
c = func_1("kato",data_1,"eee")
print(c)
