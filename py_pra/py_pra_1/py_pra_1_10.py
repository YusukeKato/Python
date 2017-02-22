# 2016.4.21
# python
# turtle_4

from turtle import *

while True:
    forward(200)
    left(170)
    # position_condetions
    if abs(pos()) < 1:
        break

