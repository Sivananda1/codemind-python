import math
def Per(x):
    s=int(math.sqrt(x))
    return s*s==x
n=int(input())
r1=5*(n*n)+4
r2=5*(n*n)-4
if Per(r1) or Per(r2):
    print(True)
else:
    print(False)