st=input()
nu=0
for i in range(len(st)):
  if(st[i].isdigit() or st[i].isalpha() or st[i]==' '):
    continue
  else:
    nu=nu+1  
print(nu)
