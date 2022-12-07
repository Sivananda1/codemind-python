s=input()
cnt=1
for i in range(1,len(s)):
    if s[i].isupper():
        cnt+=1
print(cnt)