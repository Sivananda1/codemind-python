a=input()
b=input()
s=[]
for i in a:
    if b in i:
        s.append(i)
if len(s)==0:
    print(-1)
else:
    print(len(s))