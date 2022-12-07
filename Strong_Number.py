n=int(input())
n1=n
s=1
k=0
while n>0:
    d=n%10
    while d!=0:
        s*=d
        d=d-1
    #print(s)
    k+=s
    s=1
    n=n//10
if n1==k:
    print("The number",n1,"is a strong number")
else:
    print("The number",n1,"is not a strong number")