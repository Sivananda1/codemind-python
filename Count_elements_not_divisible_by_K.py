a,b=map(int,input().split())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i%b!=0:
        s.append(i)
print(len(s))