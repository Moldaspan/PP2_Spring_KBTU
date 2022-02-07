a = input()
cnt = 0
a = a[::-1] #1100 ---> 0011
def rec(i):
    global cnt 
    if (len(a) == i):
        return
    cnt += int(a[i]) * (2**i)    
    return rec(i+1)

rec(0)
print(cnt)