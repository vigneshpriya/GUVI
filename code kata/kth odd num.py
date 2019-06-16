n,m=map(int,input().split())
o=list(map(int,input().split()))
p=[]
for i in o:
  if(i%2!=0):
    p.append(i)
print(p[m-1])
