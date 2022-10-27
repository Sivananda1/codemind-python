n=int(input())
l=list(map(int,input().split()))
s=max(l)
if s<n:
    print("YES")
else:
    print("NO")
