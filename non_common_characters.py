s=input()
s1=input()
d=[]
s=s.lower()
s1=s1.lower()
for i in range(len(s)):
    if s[i] not in s1 and s[i] not in d and s[i]!=" ":
        d.append(s[i])
for i in range(len(s1)):
    if s1[i] not in s and s1[i] not in d and s1[i]!=" ":
        d.append(s1[i])
d.sort()
if len(d)==0:
    print(-1)
else:
    print("".join(d))