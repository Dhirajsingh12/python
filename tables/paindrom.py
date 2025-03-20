n=int(input("enter the number="))
k=n
m=0
while(n>0):
    r=n%10
    m=m*10+r
    n=n//10
if(m==k):
    print("palindrom number")
else:
    print("this is not paindrom number")