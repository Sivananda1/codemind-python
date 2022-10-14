n=int(input())
s=[]
t=[]
for i in range(n//2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s.append(i)
for k in range(n,n*2):
    for l in range(2,i):
        if k%l==0:
            break
    else:
        t.append(k)
v=max(s)
u=min(t)
if n-u <= v-n:
    print(n-v)
else:
    print(u-n)