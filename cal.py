#!/usr/bin/python3

import math


# 计算矩形面积函数
def area(width, height):
    return width * height


# 计算圆面积函数
def area2(radius):
    return math.pi * radius * radius


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")

h = int(input("请输入长度："))
w = int(input("请输入宽度："))
print("width =", w, " height =", h, " area =", area(w, h))

r = int(input("请输入半径："))
print("radius = ", r, " area = ", area2(r))
