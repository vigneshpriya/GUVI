st1, st2 = input().split()
co = 0
for i in range(len(st1)):
  if st1.count(st1[i]) == st2.count(st2[i]):
    co += 1
if co == len(st1):
  print ("yes")
else:
  print ("no")
