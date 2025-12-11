# Ujal Neupane
# 
# print ("Hello World")
# print("Nischal Giri")
# name = input("Enter your name\t");
# print (name)
# Only thing wrapped with "" or ''

#Variable
#-> Variable are the programmer defined area to store data

#Rule for defining variable
# 1. Never start a variable name with number or from the symbol except _
# 2. Always use snake or kebab case naming convention

# age = input("Enter your age")
# print ("Age =" + age)

# college = "Ratna Rajya Laxmi Campus"
# print(college)

# input keyword is used to take input from the user
# Syntax: input("message")

# address = input("Enter the address:")
# print(address)

# Comments are simply the notes for the programmers.
# Comments in python are written after # 

# num1 = input("Enter a number")
# num2 = input("Enter another number")
# print(int(num1)+int(num2))

#or 

# age = int(input("Enter your age"))
# print("Your age is: " + age)  erro occur here 


# input always returns the value in string data type so it did concadination not 
# naming convention
# 1.PascalCase 2.camelCase 3.snake_case 4.kebab-case

#Type casting - converting from one data type to another

# age = float(input("Enter your age"))
# print("Your age is:\t"+age)



# Task 1
# Take two number as input and perform +,-,*,/




num1 = input("Enter a numer")
num2 = input("Enter another number")

#Addition

print("Addition:\t"+int(num1)+int(num2))

#Substraction
print("Substraction:\t"+int(num1)-int(num2))

#Multiplication
print("Multiplication:\t"+int(num1)*int(num2))

#Division
print("Division"+int(num1)/int(num2))

#Division if num2 =0

if(num2==0):
    print("Num2 cannot be zero")