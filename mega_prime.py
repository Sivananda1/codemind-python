def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
t=int(input())
if prime(t):
    while t:
        if prime(t%10)!=True:
            print("Not Mega Prime")
            break
        t=t//10
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")