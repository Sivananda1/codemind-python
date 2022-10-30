n=input()
s=n.split()
c=0
for i in s:
    if c<len(i):
        c=len(i)
print(c)