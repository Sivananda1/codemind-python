n=input()
s=n.split()
c=0
t=[]
for i in s:
    if c<len(i):
        t.append(len(i))
print(max(t))