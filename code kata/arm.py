num=int(input())
r1=0
tem=num
while(tem>0):
  d=tem%10
  r1+=d**3
  tem//=10
  
if num==r1:
  print("yes")
else:
  print("no")
