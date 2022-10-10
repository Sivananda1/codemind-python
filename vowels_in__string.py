n=input()
v=['a','e','i','o','u','A','E','I','O','U']
s=[]
t=[]
for i in n:
    if i in v:
        s.append(i)
for j in s:
    if j not in t:
        t.append(j)
if len(t)==0:
    print(-1)
else:
    print(*t)