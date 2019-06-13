a1,b1=(input().split())
a1=int(a1)
b1=int(b1)
for num in range(a1+1,b1):
  if num>1:
    for i in range (2,num):
      if (num%i==0):
        break
    else:
      print(num,end=" ")
