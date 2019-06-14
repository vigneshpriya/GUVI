n=int(input())
li=list(map(int,input().split()))
if(n==len(li)):
  li.sort()
  med=n//2
print(li[med])
