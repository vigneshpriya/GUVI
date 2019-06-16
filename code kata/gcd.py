num1,num2=map(int,input().split())
def GCD(num1,num2):
    if(num2==0):
        return num1
    else:
        return GCD(num2,num1%num2)
j=GCD(num1,num2)
print(j)
