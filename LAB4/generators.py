#1)
from pkg_resources import yield_lines


def square(n):
    for i in range(1, n + 1):
        yield i**2
n = int(input())
for i in square(n):
    print(i, end = ' ')
print()
print("-" *40)

#2)
from os import sep
a = int(input())

def gen():
    for i in range(a+1):
        if i % 2 == 0:
            yield i

print(*gen(), sep=",")
print("-" *40)

# 3)
n = int(input())
def gen():
    for i in range(n +1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for i in gen():
    print(i , end = ' ')
print()
print("-" *40)

#4)
a, b = map(int, input().split())
def squares():
    for i in range(a, b + 1):
        yield i**2

for i in squares():
    print(i, end = ' ')

print()
print("-" *40)

#5)
def gen(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for i in gen(n):
    print(i, end = ' ')
