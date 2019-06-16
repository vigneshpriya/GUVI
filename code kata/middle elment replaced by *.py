Sti=list(input())
if len(Sti)%2==0:
    Sti[int(len(Sti)/2)] ='*'
    Sti[int(len(Sti)/2)-1]='*'
else:
    Sti[int(len(Sti)/2)] ='*'
for i in range(0,len(Sti)):
    print(Sti[i],end='')
