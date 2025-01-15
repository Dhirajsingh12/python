# find the class
num1=5
num2=2.0
num3=1+2j
print(num1,"belongs to class",type(num1).__name__)
print(num2,"belongs to class",type(num2).__name__)
print(num3,"belongs to class",type(num3).__name__)

#even and odd number
num=int(input("enter the number"))
if (num%2==0):
    print("number is even")
else:
    print("number is odd")

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

