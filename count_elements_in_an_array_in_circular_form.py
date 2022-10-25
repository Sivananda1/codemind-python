n=int(input())
l=list(map(int,input().split()))
l1=l[0:2]
l=l+l1
c=0
for i in range(len(l)-2):
    if l[i]%2==0 and l[i+2]%2==1:
        c+=1
    elif l[i]%2==1 and l[i+2]%2==0:
        c+=1
print(c)