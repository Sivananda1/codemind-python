n=int(input())
for i in range(n):
    a=input()
    p=list(a)
    s=[]
    for i in a:
        if i.isnumeric():
            s.append(i)
    if len(s)==len(p):
        print(True)
    else:
        print(False)