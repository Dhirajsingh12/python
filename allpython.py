
# 1. Python program to Swap Two Variables.

x = 10
y = 50
temp = x
x = y
y = temp

print("Value of x:", x)
print("Value of y:", y)
#
x=10
y=50
print=("print befor swapping")
print=(x,y)
x,y=y,x
print=("after swapping x",x,"after swapping y",y)





# 2.Python Program to Genrate a Random Numaber.

# import random
#num = random.random()
#print(num)




# 3.Python Program to Convert Kilometers to Miles.


# 4. Python Program to Convert Celsius to Fahrenheit.
celsius = 37.5

fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


# 5. Python Program to Check if a Number is Positive, Negative or 0.

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")



# 6. Python Program to Check if n Number is Odd or even.
num= int(input("enter the number"))
if num % 2==0:
   print("number is even")
else:
   print("number is odd")

# Python program to check if year is a leap year or not

year = 2000


if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))


elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))


else:
    print("{0} is not a leap year".format(year))
    
    
    
    # 
  # Python program to find the largest number among the three input numbers

num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)






# Program to check if a number is prime or not

num = 29
flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
   
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
        
        
        
        
#
# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
           
           
           
           
#
# Python program to find the factorial of a number

num = 7

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   
   
   
   
   
   #Python Program to Display the multiplication Table.

num = 12

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
   
   
   
   
   #Python Program to Print the fabonacci sequence
n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()



#Python Program to Check Armstrong Number

num = int(input("Enter a number: "))

sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")




#Python Program to Find Armstrong Number in an Interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   order = len(str(num))
    
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
       
   
       
# Python Program to find the sum of Natural Number  

num=int(input("enter the number"))

if num<0:
    print("enter the positive no :")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
print("sum of number :",sum)
