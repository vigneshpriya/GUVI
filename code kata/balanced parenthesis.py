    
st=input()
li=list(st)
if(li[0]=='(' and li[-1]==')'):
    if(li.count('(')==li.count(')')):
        print("yes")
    else:
        print("no")
else:
    print("no")
