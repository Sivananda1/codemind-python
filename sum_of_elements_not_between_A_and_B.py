n=int(input())
s=[]
t=0
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        s.append(l[i])
for i in s:
    t+=i
print(t)