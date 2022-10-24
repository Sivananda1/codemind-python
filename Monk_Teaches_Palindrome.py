n=int(input())
for i in range(n):
    a=input()
    k=a.lower()
    b=list(k)
    c=b[::-1]
    if (b!=c):
        print("NO")
    elif (b==c) and (len(b)%2==0):
        print("YES EVEN")
    elif (b==c) and (len(b)%2==1):
        print("YES ODD")