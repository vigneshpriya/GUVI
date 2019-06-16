n=int(input())
m=list(map(int,input().split()))
o=m[:]
o.sort()
for vi in range(0,len(m)):
  if(m[vi]!=o[vi]):
    print(vi)
    break
