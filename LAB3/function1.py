#1)
grams = int(input())
def ff(grams):
    ounces = 28.3495231 * grams
    return ounces

#print(ff(grams))

#2)
f = int(input())
def temp(f):
    return (5/9)*(f - 32)
    
#print(temp(f))

#3)
heads, legs = map(int,input().split())

def solve(heads, legs):
    for tauyk in range(heads + 1):
        koyan = heads - tauyk
        if tauyk*2 + koyan*4 == legs:
            return str(tauyk) + ' ' + str(koyan)
            
heads = 35
legs = 94
#print(solve(heads, legs))

#4)
import math
def filter_prime(arr):
    l = []
    for i in arr:
        ok = True
        num = int(math.sqrt(i))
        for j in range(2, num+1):
            if i % j == 0:
                ok = False
                break
        if ok == True:
            l.append(i)    
    return l

arr = list(map(int, input().split()))
#print(filter_prime(arr))

#6)
def rever(s):
    l = s.split()
    l = l[::-1]
    return l

s = input()
#print(*rever(s))

#7)
def has_33():
    numbers =  list(map(int, input().split()))
    for i in range(len(numbers)-1):
        if (numbers[i] == 3 and numbers[i+3] == 3):
            return True
    return False
#print(has_33())

#8)
def agentt_007():
    numbers = list(map(int, input().split()))
    s = ''
    for i in numbers:
        if(i == 0 or i == 7):
            s+= str(i)
    for i in range(len(s)- 2):
        if(s[i] == '0' and s[i+1] == '7'):
            return True
        else:
            return False
#print (agent_007())

#9)
r = int(input())
from math import pi

def sphere(r):
    return 4/3* pi* r**3

#print(sphere(r))

#10)
l = list(map(int,input().split()))
def unique_list(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n
#print(unique_list(l))
#11)
def rev(s):
    palindrom = True
    if (s != s[::-1]):
        return False
    return True

str=input()
if rev(str):
    print("T R U E")
else:
    print("F A L S E")
    
#12)
def histogram(array): 
    for i in array: 
        print('*' * i)
