with open('input.txt', 'r') as f:
    x = f.readlines()
cnt = 0
for line in x:
    if line != '\n':
        cnt+=1
print('number of lines:', cnt)