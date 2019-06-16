liss=[str(x)  for x in input()]
li1=['a','e','i','o','u']
a=0

for i in liss:
  if(i in li1):
    a=1
if(a==1):
  print("yes")
else:
  print("no")
