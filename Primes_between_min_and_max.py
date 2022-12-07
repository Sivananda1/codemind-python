def primes(n):
    if n==1:
        return False
    for j in range(2,n):
        if n%j==0:
            return False
    return True
p=int(input())
n=list(map(int,input().split()))
cnt=0
a=n.index(min(n))
b=n.index(max(n))+1
if a>b:
    a,b=b,a
for i in range(a,b):
    if primes(n[i]):
        cnt+=1
print(cnt)