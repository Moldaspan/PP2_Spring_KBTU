s = input()
def tolower():
    t = ""
    for i in s:
        if(i >= 'A' and i <= 'Z'):
            i = chr(ord(i) + 32)
        t += i
    print(t)
tolower()