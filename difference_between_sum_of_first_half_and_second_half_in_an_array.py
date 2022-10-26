n=int(input())
l=list(map(int,input().split()))
s=len(l)//2
s1=0
s2=0
for i in range(len(l)):
    if i>=s:
        s1+=l[i]
    else:
        s2+=l[i]
print(s1-s2)