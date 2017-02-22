# 2016.4.23
# Python
# turtle

from turtle import *

def step_up():
    length = 10
    angle = 90
    for i in range(10):
        forward(length)
        left(angle)
        forward(length)
        right(angle)

def step_down():
    length = 10
    angle = 90
    for j in range(10):
        forward(length)
        right(angle)
        forward(length)
        left(angle)

def circle():
    length = 0.5
    angle = 1
    for k in range(360):
        forward(length)
        right(angle)
        
        
        

step_up()
step_down()
circle()
    
    
