n=int(input())
tem=n
re=0
while(n>0):
  di=n%10
  re=re*10+di
  n=n//10
print(re)
