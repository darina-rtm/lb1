# -*- coding: cp1251 -*-
from math import *
a = float(input('Введите параметр а: '))
x = float(input('Введите значение x: '))
z1=sin(a)+cos(2*x-a)/(cos(a)-sin(2*x-a))
print("{0:.2f} {1:.2f} {2:.4f}".format(a, x, z1))
z2=1+sin(2*x)/(cos(2*x))
print("{0:.2f} {1:.4f}".format(x, z2))
print("Hello World")
