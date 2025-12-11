#Perform Arithmetic Operation

num1 = (input("Enter a number:\t"))
num2 = (input("Enter another number:\t"))

#For Addition
print("Addition of "+num1+ " and "+num2+" is: "+str(int(num1)+int(num2)))

#For Subtraction
print("Subtraction of "+num1+" and "+num2+" is: "+str(int(num1)-int(num2)))

#For Multiplication
print("Multiplication of "+num1+" and "+num2+" is: "+str(int(num1)*int(num2)))

#For Division
if(int(num2)!=0):
    print("Division of "+num1+" and "+num2 +" is: "+str(int(num1)/int(num2)))
else:
    print("ZeroDivisionError!!!")