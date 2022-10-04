n=int(input())
for i in range(n):
    a=input()
    s=0
    l=list(a)
    l.reverse()
    for j in range(len(l)):
        s+=int(l[j])*2**j
    print(s)