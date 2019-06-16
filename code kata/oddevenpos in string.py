st=input()
x1=""
y1=""
for i in range(0,len(st)):
  if (i%2!=0):
    x1=x1+st[i]
  else:
    y1=y1+st[i]
print(y1,x1)
