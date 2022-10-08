n=input()
v=['a','e','i','o','u','A','E','I','O','U']
s=[]
for i in n:
    if i in v:
        s.append(i)
if len(s)==0:
    print(0)
else:
    print(len(s))