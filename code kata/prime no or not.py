nu=int(input())
if nu>0:
  for i in range(2,nu):
    if(nu%i==0):
      print("no")
      break
  else:
      print("yes")
else:
  print("no")
