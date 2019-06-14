num=int(input())
value=map(int,list(input().split()))
so=sorted(value)
for x in range(0,len(so)):
  print(so[x], end=' ')
