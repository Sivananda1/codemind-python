n=input()
c=0
s=[]
s.append(n)
for i in s:
    w=i.split(' ')
    c+=len(w)
print(c)
