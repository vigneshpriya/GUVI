st=input()
nu=[]
for i in st:
  if (i.isnumeric()):
    nu.append(i)
print(*nu,sep='')
