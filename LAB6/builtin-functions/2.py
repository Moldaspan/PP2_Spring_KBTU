a=input()
upper=0
lower=0
for i in a:
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
print(lower, upper)