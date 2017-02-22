# 2016.4.23
# Python

#型をあまり考えなくて良いのは楽

# 意味はない、何もない nothing_idea
class splatoon:
    def __init__(self,data_1,data_2,data_3):
        self.data_1 = data_1
        self.data_2 = data_2
        self.data_3 = data_3
    def squid(self):
        return self.data_1 + self.data_2 + self.data_3

ink = splatoon("Splatoon","_","Squid")  # string
print(ink.squid())
yellow = splatoon(2,4,1)    # value(number)
print(yellow.squid())

