n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
    if l[i]==0 or l[i]==1:
        s.append(l[i])
if len(s)==len(l):
    print(True)
else:
    print(False)