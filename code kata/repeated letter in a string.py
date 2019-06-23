sst = input()
co= []
for i in range(len(sst)):
  co.append(sst.count(sst[i]))
i = co.index(max(co))
print (sst[i]
