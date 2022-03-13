import re
a = input()
b = re.split(r'[A-Z]+', a)
print(*b)