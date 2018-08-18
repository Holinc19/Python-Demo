#!/usr/bin/python3
# -*- coding: gbk -*- 

print("Hello, World!")

if True:
    print("True")
else:
    print("False")

str = 'Runoob'
print(str)
print('------------------------------')
print('hello\nrunoob')
print(r'hello\nrunoob')

input("\n\n按下 enter 键后退出。")

import sys

print('================Python import mode==========================');
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
