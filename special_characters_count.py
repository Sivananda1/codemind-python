n=input()
s=0
l='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in n:
    i=i.strip()
    if i not in l:
        s+=1
print(s)