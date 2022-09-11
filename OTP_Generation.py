n=int(input())
s=[]
while n:
    r=n%10
    n=n//10
    s.append(r)
a=s[::-1]
for i in a:
    if i%2==1:
        print(i**2,end='')
