NU1, NU2 = list(map(int,input().split()))
M = 0
for i in range(NU1):
  if NU2**i == NU1:
    M = 1
    break
if M == 1:
  print("yes")
else:
  print("no")
