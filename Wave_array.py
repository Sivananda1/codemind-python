n=int(input())
v=list(map(int,input().split()))
cnt=0
for i in range(len(v)-3):
    if (v[i]<v[i+1] and v[i+1]>v[i+2]) or (v[i]>v[i+1] and v[i+1]<v[i+2]):
        continue
    else:
        print("no")
        break
else:
    print("yes")