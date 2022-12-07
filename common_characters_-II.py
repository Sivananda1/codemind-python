s=input()
s1=input()
d=[]
s=s.lower()
s1=s1.lower()
#print(s,s1)
for i in range(len(s)):
    if s[i] in s1 and s[i] not in d and s[i]!=" ":
        d.append(s[i])
print(len(d))