aa,bb,cc=map(int,input().split())
su=0
for i in range (1,cc+1):
  su+=aa+(i-1)*bb
print(su)
