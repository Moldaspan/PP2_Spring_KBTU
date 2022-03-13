import re
a = input()
pattern = r'[a-z][^_]*'

b = re.findall(pattern, a)
t = ""

for i in b:
    t += i.capitalize()

print(t)

#my_name_is_yersultan ----> MyNameIsYersultan