n=int(input())
l=list(map(int,input().split()))
x=int(input())
l1=[]
for i in l:
    t=i+x
    if t>=max(l):
        l1.append("True")
    else:
        l1.append("False")
print(*l1)