x1,y1=(input().split())
x1=int(x1)
y1=int(y1)
for i in range(x1,y1):
  sum=0
  te=i
  while(te>0):
    e=te%10
    sum+=e**3
    te//=10
    if(i==sum):
      print(i,end=' ')
