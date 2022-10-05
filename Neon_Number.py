n=int(input())
s=n*n
t=0
while s:
    r=s%10
    t+=r
    s=s//10
if t==n:
    print("Neon Number")
else:
    print("Not Neon Number")