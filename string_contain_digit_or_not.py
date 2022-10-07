n=input()
s=[]
for i in n:
    if i.isnumeric():
        r=int(i)
        s.append(i)
if len(s)==0:
    print("Doesn't contain digit")
else:
    print('Contains',len(s),'digit')