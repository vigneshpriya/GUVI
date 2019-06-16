li=list(map(int,input().split()))
m=0
n=0
while True:
  if (li[1] * li[0]) == (m*m):
    print("yes")
    n=n+1
    break
  if (li[1] * li[0]) < (m*m):
    print("no")
    break
  m=m+1
