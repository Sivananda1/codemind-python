a,b,c=map(int,input().split())
s=[]
for i in range(a,b+1):
    if i%c==0:
        s.append(i)
print(len(s))