import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def rev(n):
    b=str(n)
    return int(b[::-1])
t=int(input())
l=[]
for i in range(t*t):
    if isprime(i) and i==rev(i):
        l.append(i)
        if i>t:
            print(i)
            break