import re
a = input()
pattern ='[a-z]+_[a-z]+'
b = re.search(pattern, a)
print(b)