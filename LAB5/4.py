import re

a = input()
pattern = r'[A-Z][a-z]{2,}'
print(re.search(pattern, a))