s=input()
s1=input()
d=[]
s=s.lower()
s1=s1.lower()
s=s.split()
s1=s1.split()
for i in range(len(s1)):
    if s1[i] in s:
        d.append(s1[i])
if len(d)==0:
    print(-1)
else:
    print(len(d))