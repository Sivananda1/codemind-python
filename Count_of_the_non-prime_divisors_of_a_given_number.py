n=int(input())
s=[]
t=[]
for i in range(1,n+1):
    if n%i==0:
        s.append(i)
for j in range(2,n):
    for k in range(2,j):
        if j%k==0:
            break
    else:
        t.append(j)
for l in t:
    if l in s:
        s.remove(l)
print(len(s))