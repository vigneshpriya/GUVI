b1=input()
b1=b1.lower()
nm=""
for n in b1:
  if n not in nm:
    nm=nm+n
if (b1==nm):
  print("Yes")
else:
  print("No")
