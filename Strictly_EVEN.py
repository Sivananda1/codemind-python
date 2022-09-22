n=int(input())
l=list(map(int,input().split()))
t=True
for i in range(len(l)):
    if l[i]%2==0 and i%2:
        print(False)
        t=False
        break
if t==True:
    print(True)