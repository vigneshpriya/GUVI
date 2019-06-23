ll,rr=map(int,input().split())
for i in range(1,10001):
  if((i%ll==0) and (i%rr==0)):
    print(i)
    break
