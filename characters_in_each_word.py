n=input()
s=n.split()
r=[]
for i in s:
    r.append(len(i))
print(*r)