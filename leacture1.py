#   Author: Muhammad Shoaib Khan
#   in this leacture we will learn about python basics like print statement, data types,
#    comments,variables, operators, type conversion, input function and practice set
# part 1
# print statement is used to print anything on console
print ("Hello World")
print ("Muammad Shoaib Khan Kulachi BScs 7th Semester")

# part 2
# Data Types in python like int, float, string, boolean , complex , list, tuple, dictionary
Name="Muammad Shoaib Khan Kulachi"
RollNo="BScs 7th Semester"
age=18
preice=100.5
print("My Name is:",Name)
print("My Roll No is:",RollNo)
print(age)
print(preice)
print(type(Name))
print(type(RollNo))
print(type(age))
print(type(preice))
if age>=18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")

# part 3
# Variables in python
a=10
b=20
sum=a+b
print("Sum of a and b is:",sum)
print("Sum of",a,"and",b,"is:",sum)

a=10
b=-a
print("Value of b is:",b)

name="Muammad Shoaib Khan Kulachi"
print("My Name is:",name)
age=23
print("My age is:",age)

both=name+" "+str(age) #concatination of string and age
print(both)

firstname="Muammad Shoaib Khan"
lastname="Kulachi"
fullname=firstname+lastname
print(fullname)

# Multi line string ko print krwane k liye 3 double/single quotes use krte hain 
poem='''Twinkle, Twinkle, Little Star
Shining bright from realms afar,
Up above the world so high,
Like a beacon in the sky.

Guiding lost ships through the night,
Casting down your silver light,
Do you dance or do you dream,
Glistening with a golden gleam?

Twinkle, twinkle, little spark,
Glowing softly in the dark,
Though you seem so small to me,
You're a sun in mystery!

Twinkle, twinkle, little star,'''

print(poem)

# part 4 Operators in python
#  type=A types of arithmetic operators
a=10
b=20
print("Sum of a and b is:",a+b)
print("Subtraction of a and b is:",a-b)
print("Multiplication of a and b is:",a*b)
print("Division of a and b is:",a/b)
print("Floor division of a and b is:",a//b)
print("Modulo of a and b is:",a%b)
print("Exponential of a and b is:",a**b)

# part 5 type=B types of comparison operators
a=10
b=20
print("a==b is:",a==b) # == is used for comparison
print("a!=b is:",a!=b) # != is used for not equal to
print("a>b is:",a>b)  # > is used for greater than 
print("a<b is:",a<b)  # < is used for less than
print("a>=b is:",a>=b) # >= is used for greater than equal to
print("a<=b is:",a<=b) # <= is used for less than equal to


# part 6 type=C types of assignment operators
a=5
b=2
a+=b # a=a+b
print("a+=b is:",a)
a-=b # a=a-b
print("a-=b is:",a)
a*=b # a=a*b
print("a*=b is:",a)
a/=b # a=a/b
print("a/=b is:",a)
a%=b # a=a%b
print("a%=b is:",a)
a**=b # a=a**b
print("a**=b is:",a)
a//=b # a=a//b
print("a//=b is:",a)


# part 7 type=D types of logical operators
a=5
b=2
print("a and b is:",a and b) # and operator
print("a or b is:",a or b) # or operator
print("not a is:",not a) # not operator


# part 8 is type conversion
a=10
b=20.5
c=a+b
print("Sum of a and b is:",c) # int+float= float
print("Sum of a and b is:",int(c)) # int+float= float
print("Sum of a and b is:",str(c))  # int+float= float
print("Sum of a and b is:",float(c)) # int+float= float
print("Sum of a and b is:",complex(c)) # int+float= float


# part 9 is input function
name=input("Enter your name:") # input function is used to take input from user
age=int(input("Enter your age:")) # input function is used to take input from user int is used to convert string into integer
marks=float(input("Enter your marks:")) # input function is used to take input from user float is used to convert string into float
print("Your name is:",name)
print("Your age is:",age)
print("Your marks is:",marks)

# part 10 is a prectice set
# Q1 write a program to input 2 numbers and print their sum
a=int(input(" Enter First Number:"))
b= int(input("Enter Second Number:"))
sum=a+b
print("Sum is:",sum)

# Q2 write a program to input side of square and print area of square
side=float(input("Enter side of square:"))
area=side*side
print("Area of square is:",area)

# Q3 WAP to input 2 floating numbers and print their average
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
avg=(a+b)/2
print("Average is:",avg)

