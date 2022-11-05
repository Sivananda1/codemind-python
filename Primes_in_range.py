def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
t1=int(input())
t2=int(input())
c=0
for i in range(t1,t2+1):
    if isprime(i):
        c+=1
print(c)