n = int(input())
st = input()
if st == "k":
    m = str(input())
    num = "{:." + m + "f}"
    print(num.format(n / 1024))
else:
    print(n * 1024)