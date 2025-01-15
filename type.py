'''num1=5
print("num1",num1,"belongs to class",type(num1).__name__)
num2=3.6
print("num2",num2,"belongs to class",type(num2).__name__)
num3=1+3j
print("num3",num3,"belongs to class",type(num3).__name__)'''
import math
num1=float(input("enter the frist number"))
num2=float(input("enter the second number"))
sum=num1+num2
print("sum of two number",sum)
sqrt=math.sqrt(sum)
print("sqrt of sum",sqrt)
#
num=int(input("enter the number"))
if num==0 or num==1:
 print("factorial is 1")
if num>1:
 for i in range(1,num+1):
  factorial=num*i
print("factorial",factiorial)
