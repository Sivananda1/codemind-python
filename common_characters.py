s=input()
s1=input()
d=[]
s=s.lower()
s1=s1.lower()
for i in range(len(s)):
    if s[i] in s1 and s[i] not in d and s[i]!=" ":
        d.append(s[i])
d.sort()
if len(d)==0:
    print(-1)
else:
    print("".join(d))