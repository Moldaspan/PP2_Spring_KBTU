s = input() 
t = [] 
 
for i in range(len(s)): 
    if s[i] == '[' or s[i] == '(' or s[i] == '{': 
        t.append(s[i]) 
    else: 
        if len(t) == 0: 
            print("No") 
            exit() 
        t_top = t[len(t)-1] 
        if s[i] == ')' and t_top != '(' or s[i] == ']' and t_top != '[' or s[i] == '}' and t_top != '{': 
            print("No") 
            exit() 
        t.pop() 
 
if len(t) != 0: 
    print("No") 
else: 
    print("Yes")