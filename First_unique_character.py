n=input().lower()
n=list(n)
s=[]
for i in range(len(n)):
    if n.count(n[i])==1:
        s.append(n[i])
if len(s)==0:
    print(-1)
else:
    print(s[0])