import re
a = input()
pattern = r'([a-z])([A-Z])'
print(re.sub(pattern, r'\1 \2', a))

#MyNameIsYersultan ---> my_name_is_yersultan