num1,num2 = map(int,input().split())
count=0
for i in range(num1,num2+1):
  if(i>1):
    for num in range(2,i):
      if(i%num)==0:
        break
    else:
      count=count+1
print (count)
