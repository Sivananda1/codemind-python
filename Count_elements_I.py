a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
t=0
for i in l1:
    for j in l2:
        if i==j:
            s.append(i)
t=set(s)
print(len(t))