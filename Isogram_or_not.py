n=input()
s=sorted(n)
t=[]
for i in s:
    if i not in t:
        t.append(i)
if len(s)==len(t):
    print(True)
else:
    print(False)