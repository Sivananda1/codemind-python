import math
def per(x):
    s=int(math.sqrt(x))
    return s*s==x
n=int(input())
r1=5*(n*n)+4
r2=5*(n*n)-4
if per(r1) or per(r2):
    print(True)
else:
    print(False)