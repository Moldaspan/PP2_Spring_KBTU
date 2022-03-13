import re
a = input()
pattern = r'a.+b$'
print(re.search(pattern, a))