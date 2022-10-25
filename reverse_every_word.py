n=input()
l=n.split()
s=[]
for i in l:
    s.append(i[::-1])
print(*s)