# 2016.4.21
# Python
# turtle_2

from turtle import *

# draw_branch 枝
def branch(length):
    if length < 10:
        return
    forward(length)
    left(30)
    branch(length/2)
    right(60)
    branch(length/2)
    left(30)
    forward(-length)

for i in range(8):
    branch(200)
    left(45)
