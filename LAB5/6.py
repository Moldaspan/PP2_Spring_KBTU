import re
a = input()
b = re.sub(r'[\s,.]+', ':', a)
print(b)