a=[[1,2,3,],[4,5,6],[7,8,9]]
b=[[7,8,9],[4,7,8],[3,2,1]]
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            res[i][j]*=a[i][k]+b[k][j]
for r in res:
 print(r)

 #matrix addition
 
a=[[1,2,3,],[4,5,6],[7,8,9]]
b=[[7,8,9],[4,7,8],[3,2,1]]
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            res[i][j]+=a[i][k]+b[k][j]
for r in res:
 print(r)
#sqrt using newton
def newtonsqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        print(better)
        print(approx)
        better=0.5*(approx+n/approx)
        return approx
print(newtonsqrt(64))

#largest number of the list
a=[10,76,23,67,28,50]
largest=a[0]
for value in a:
    if value > largest:
        largest=value
print(largest)
'''
#conversion of list to tuple
a=[10,76,23,67,28,50]
print("list",a)
tuple1=tuple(a)
print("tuple",tuple1)
print(list1=list(tuple1))
print(list1.update([100]))
'''
