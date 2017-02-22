# 2016.4.21
# python
# turtle_5

from turtle import *

degree = 1
distance = 50
# yokuwakaranaizukei
for i in range(50):
    forward(distance)
    right(degree)
    degree += 2
    distance -= 1
