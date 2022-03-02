import math
#1)
degree = float(input('Input degree:'))
radian = degree * (math.pi/180)
print('Output radian:', radian)
print('-' * 30)

#2)
h = int(input('Height:'))
a = int(input('Base, first value:'))
b = int(input('Base, second value:'))
s = h*(a + b)/2
print('Expected Output:', s)
print('-' * 30)

#3)
from math import tan, pi
sides = int(input('Input number of sides:'))
length = int(input('Input the length of a side:'))
area = sides * length**2/4*tan(pi / sides)
print('The area of the polygon is',round(area))
print('-' * 30)

#4)
length = float(input('Length of base:'))
height = float(input('Height of parallelogram:'))
area = length * height
print('Expected Output:', area)
print('-' * 30)

