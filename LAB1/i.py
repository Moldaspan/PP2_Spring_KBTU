n = int(input())
m = []
for i in range(n):
    s = input()
    if("@gmail.com" in s):
        index = s.find("@gmail.com")
        s = s[0:index]
        m.append(s)

for i in m:
    print(i)