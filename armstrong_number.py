n=int(input("enter the number ="))

m=len(str(n))
sum=0
temp=n
while temp>0:
    d=n%10
    sum+=d**m
    temp//=10
if(n==sum):
    print("this is armstrong number")
else:
    print("this is not armstrong number")
    