n=int(input())
c=0
l=list(map(int,input().split()))
#print(l)
for i in range(1,len(l)-1):
    if (l[i-1]%2==1 and l[i+1]%2==0):
        c+=1
    elif(l[i-1]%2==0 and l[i+1]%2==1):
        c+=1
print(c)