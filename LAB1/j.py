x = list(map(str, input().split()))
def func():
    y = ""
    for i in x:
        if(len(i) >= 3):
            y += i + " "
    return y        

print(func())