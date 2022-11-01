n=input().lower()
n=list(n)
s=[]
for i in range(len(n)):
    if n.count(n[i])==1 and n[i]!=' ':
        s.append(n[i])
print("".join(sorted(s)))