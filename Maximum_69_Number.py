num=int(input())
if num==9999 or num==999 or num==99 or num==9:
    print(num)
else:
    n=list(str(num))
    k=[]
    for i in range(len(n)):
        n=list(str(num))
        if n[i]=="9":
            n[i]="6"
        else:
            n[i]="9"
        k.append(''.join(map(str,n)))
    print (max(k))