st1,st2=input().split()
co=0
for i in range(0,len(st2)):
  if(st1[i]!=st2[i]):
    co=co+1
if (co==1):
  print("yes")
else:
  print("no")
