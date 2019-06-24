nu1=list(map(int,input().split()))
nu2=list(map(int,input().split()))
for i in range(0,nu1[1]):
  nu2=[nu2[-1]] + nu2[:-1]
print(*nu2,end=' ')
