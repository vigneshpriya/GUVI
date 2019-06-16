import math
l,m=input().split()
L1=int(l)
M1=int(m)
num=math.gcd(L1,M1)
print((L1*M1)//num)
