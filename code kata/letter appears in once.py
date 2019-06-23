num=int(input())
li=list(map(int,input().split()))
co=[]
for i in li:
  if(li.count(i)>1):
    co.append(i)
  else:
    print(i)

