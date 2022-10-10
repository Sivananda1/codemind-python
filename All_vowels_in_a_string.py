n=input()
v=['a','e','i','o','u']
t=set(v)
s=[]
for i in n:
    if i in v:
        s.append(i)
k=set(s)
if len(k)==len(t):
    print(True)
else:
    print(False)