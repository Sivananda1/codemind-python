s=input()
k=""
for i in s:
    if i=='0':
        k+='000'
    elif i=='1':
        k+='001'
    elif i=='2':
        k+='010'
    elif i=='3':
        k+='011'
    elif i=='4':
        k+='100'
    elif i=='5':
        k+='101'
    elif i=='6':
        k+='110'
    elif i=='7':
        k+='111'
k=k[k.index('1'):]
print(k)