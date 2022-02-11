s = str(input())  
if " " not in s:  
    x = int(input())  
    n = int(s)  
else:  
    s = s.split()  
    n = int(s[0])  
    x = int(s[1]) 
arr = [] 
for i in range(n): 
    num =  x + 2 * i 
    arr.append(num) 
num = arr[0] 
 
for i in range(1, len(arr)): 
    num = num ^ arr[i] 
print(num)