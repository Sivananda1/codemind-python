n=input()
s=[]
for i in n:
    if i.isnumeric():
        r=int(i)
        s.append(r)
print(sum(s))