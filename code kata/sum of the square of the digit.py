num=int(input())
a=0
while(num!=0):  
  rem=num%10
  a=a+(rem*rem)
  num=num//10
print(a)
