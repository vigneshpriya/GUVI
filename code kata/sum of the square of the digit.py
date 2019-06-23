nu1=int(input())
a=0
while(nu1!=0):  
  rem=nu1%10
  a=a+(rem*nu1)
  nu1=nu1//10
print(a)
