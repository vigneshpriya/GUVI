num1=int(input())
num2=input()
temp=0
v=['a','e','i','o','u']
for i  inv:
  if(i in v):
    num2=num2.replace(i,'')
print(num2[::-1])
