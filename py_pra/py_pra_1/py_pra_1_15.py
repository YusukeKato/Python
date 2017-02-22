# 2016.4.22
# Python
# about_argument
# class_2

class Myclass_2:
    def __init__(self,arg_1,arg_2,arg_3):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.arg_3 = arg_3
    def method_1(self):
        self.name = ""
    def method_2(self):
        self.data = ""
    def method_3(self):
        return self.arg_1 + self.arg_2 + self.arg_3 + self.name + self.data

r1 = Myclass_2("1","2","3")
r1.name = "4"
r1.data = "5"

print(r1.method_3())

    





