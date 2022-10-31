a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i<0:
        i=i*(-1)
    s=str(i)
    if len(s)==b:
        c+=1
print(c)