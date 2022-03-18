with open('input.txt', 'r') as f:
    x = f.read()
f.close()
r = open('input3.txt', 'w')
r.write(x)
r.close()