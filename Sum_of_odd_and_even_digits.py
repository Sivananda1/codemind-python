m=int(input())
l=list(map(int,input().split()))
o=0
e=0
for i in range(len(l)):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if (o-e)==0:
    print("YES")
else:
    print("NO")