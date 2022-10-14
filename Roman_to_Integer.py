n=input()
def roman(n):
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    f=0
    for i in range(len(n)):
        if i+1 !=len(n) and d[n[i]]<d[n[i+1]]:
            f=f-d[n[i]]
        else:
            f=f+d[n[i]]
    return f
print(roman(n))