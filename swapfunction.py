#Take inputs from user for two numbers( x and y )

x=8.2
y=52

x, y = y, x 

print("before swap,value of x = ", x)
print("before swap,value of y = ", y)

temp = x
print("value of temp is :",temp)
x=y
print("value of  is :" ,temp)
y=temp
print("value of temp is :",temp)

print("after swap,the value of x is ",x)
print("after swap,the value of y is ",y)