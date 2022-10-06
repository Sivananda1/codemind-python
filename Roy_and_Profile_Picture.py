a=int(input())
b=int(input())
for i in range(b):
    c,d=map(int,input().split())
    if c<a or d<a:
        print("UPLOAD ANOTHER")
    elif c==d:
        print("ACCEPTED")
    else:
        print("CROP IT")
