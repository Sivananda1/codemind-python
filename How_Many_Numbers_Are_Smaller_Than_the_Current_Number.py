n=int(input())
l=list(map(int,input().split()))
for i in l:
    c=0
    for j in range(len(l)):
        if i>l[j]:
            c+=1
    print(c,end=" ")
            