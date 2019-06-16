nu=int(input())
aa=0
l1,r1=map(int,input().split())
for i in range(l1+1,r1):
  if(i==nu):
    aa=1
if(aa==1):   
  print("yes")
else:
  print("no")
