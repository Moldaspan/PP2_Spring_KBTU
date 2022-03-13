import re

a = input()
pattern = r'ab*'
print(re.search(pattern, a))


