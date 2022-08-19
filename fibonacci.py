n=int(input())
a,b=0,1
c=0
while c<n:
    print(a,end=' ')
    s=a+b
    a=b
    b=s
    c+=1