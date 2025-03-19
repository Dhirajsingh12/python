#leep years
y=int(input("enter the year="))
if(y%400==0 or y%4==0):
    print("this is leep year")
elif(y%100==0):
    print("this is not leep year")