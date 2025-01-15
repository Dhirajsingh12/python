
file = open('C:/Users/dhira/Desktop/dhiraj11.txt','r')
file_containes = file.read()
print(file_containes)
file_containes.split()
#for char in file_containes:
 #   print(f"'{char}',",end="")
list = [char for char in file_containes]
print(list)


