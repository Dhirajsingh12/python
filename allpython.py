x = 10
y = 50
temp = x
x = y
y = temp

print("Value of x:", x)
print("Value of y:", y)

x=10
y=50
print=("print befor swapping")
print=(x,y)
x,y=y,x
print=("after swapping x",x,"after swapping y",y)

celsius = 37.5

fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))



num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

num= int(input("enter the number"))
if num % 2==0:
   print("number is even")
else:
   print("number is odd")


year = 2000


if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))


elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))


else:
    print("{0} is not a leap year".format(year))
   

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
   

num = 12

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
   
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
        

num=int(input("enter the number"))

if num<0:
    print("enter the positive no :")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
print("sum of number :",sum)
