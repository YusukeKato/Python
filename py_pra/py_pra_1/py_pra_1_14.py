# 2016.4.22
# Python
# GOAL:Effort_of_CommentOut
# class_1

# クラス作成 Make_Class
class Myclass:
    def __init__(self,data_1,data_2,data_3):
        self.data_1 = data_1
        self.data_2 = data_2
        self.data_3 = data_3
    def result(self): # 足した結果 Sum_Result
        self.data = self.data_1 + self.data_2 + self.data_3
        return self.data

# クラスを使う Use_Myclass
res_1 = Myclass(1,2,3)
print(res_1.result())
res_2 = Myclass(4,5,6)
print(res_2.result())

# アトリビュート変更 Chage_Attribute
res_1.data_1 = 10
res_1.data_2 = 20
res_1.data_3 = 30
print(res_1.result())

# アトリビュート表示 OutPut_Attribute
print(res_1.data_1)
print(res_2.data_2)

