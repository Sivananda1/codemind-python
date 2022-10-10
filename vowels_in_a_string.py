n=input()
m=input()
k=list(n)
s=[]
v=['a','e','i','o','u','A','E','I','O','U']
for i in k:
    if i in v:
        s.append(i)
if m in s:
    print(True)
    print(k.index(m))
else:
    print(False)