n=int(input())
s=0
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        break
    s+=i
print(s)