n=int(input())
for i in range(n):
    a=input()
    s=[]
    for i in a:
       if i.isnumeric():
           r=int(i)
           s.append(r)
    if len(s)==0:
        print("No")
    else:
        print("Yes")