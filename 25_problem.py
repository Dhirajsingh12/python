def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a=int(input("enter the first number="))
b=int(input("enter the second number="))
c=int(input("enter the third number"))
print(great(a,b,c))
    