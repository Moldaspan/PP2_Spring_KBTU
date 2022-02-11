d = {'ONE':'1', 
'TWO':'2', 
'THR':'3', 
'FOU':'4', 
'FIV':'5', 
'SIX':'6', 
'SEV':'7', 
'EIG':'8', 
'NIN':'9', 
'ZER':'0'} 
task = input() 
l = '' 
for i in range(len(task)): 
    if task[i:i + 3] in d.keys(): 
        l += d[task[i: i+3]] 
    elif task[i] == '+': 
        l += '+' 
res = str(sum(list(map(int, l.split('+'))))) 
rev_dic = {key:val for val,key in d.items()} 
print(''.join(rev_dic[i] for i in res))