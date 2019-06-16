st=input()
le=False
nu=False
for i in st:
  if(i.isdigit()):
    le=True
  if(i.isalpha()):
    nu=True
if le and nu:
  print("Yes")
else:
  print("No")
