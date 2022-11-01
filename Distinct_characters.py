n=input().lower()
n=list(n)
s=[]
for i in range(len(n)):
    if n[i] not in s and n[i]!=' ':
        s.append(n[i])
print("".join(sorted(s)))