# 2016.4.21
# Python
# turtle_3


from turtle import *

# spiral
for i in range(40):
    forward(100)
    if i % 4 == 1:
        right(160)
    elif i % 4 == 3:
        right(20)
    else :
        right(10)
