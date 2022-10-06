n=int(input())
s=[]
t=[]
v=[]
while n:
    r=n%10
    s.append(r)
    n=n//10
for i in s:
    if i%2==0:
        t.append(i)
    elif i%2==1:
        v.append(i)
if len(s)==len(t):
    print("Even")
elif len(s)==len(v):
    print("Odd")
else:
    print("Mixed")
    