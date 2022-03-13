import re
a = input()
pattern = r'([a-z])([A-Z])'
x = re.sub(pattern, r'\1_\2', a).lower()
print(x)