n=int(input())
s=0
p=0
l=list(map(int,input().split()))
for i in range(1,len(l)-1):
    s+=i
    p=s//n
if i>p:
    print(i-1)
    