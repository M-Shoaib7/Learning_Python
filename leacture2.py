# part 1


# strings in python
name="Muammad Shoaib Khan Kulachi"
print(name)
len1=len(name)
print(len1) # length of string
print(type(name))


# string indexing
name="Muammad Shoaib Khan Kulachi"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
print(name[11])
print(name[12])
print(name[13])

x=10
y=5
print(x==y) # false


# string slicing
name="Muhammad Shoaib Khan Kulachi"
print(name[9:14]) # Shoaib
print(name[9:]) # Shoaib Khan Kulachi
print(name[0:])


# string functions
# these functions can not make changes in the original string
# they will return a new string 
# if you want to make changes in the original string then you have to assign it to a new variable like this
name=name.replace("Muhammad","Ali")
name="Muhammad Shoaib Khan Kulachi"
print(name.endswith("chi")) # True
print(name.startswith("Muhammad")) # True
print(name.upper()) # MUHAMMAD SHOAIB KHAN KULACHI
print(name.lower()) # muhammad shoaib khan kulachi
print(name.title()) # Muhammad Shoaib Khan Kulachi
print(name.capitalize()) # Muhammad shoaib khan kulachi
print(name.replace("Khan","Ali")) # Ali Shoaib Khan Kulachi
print(name.find("Shoaib")) # 9 find the index of the first occurrence of the string
print(name.find("Ali")) # -1 if not found it will return -1
print(name.find("n")) # find the index of the first occurrence of the string
print(name.count("a")) # 4 count the number of occurrences of the string
print(name.count("S")) # 1 count the number of occurrences of the string
print(name.count("K")) # 2 count the number of occurrences of the string
print(name.strip()) # Muammad Shoaib Khan Kulachi remove the leading and trailing spaces

# string concatenation and string formatting
a="Muhammad"
b="Shoaib"
c="Khan"
d="Kulachi"
print(a+b+c+d) # MuhammadShoaibKhanKulachi
print(a+" "+b+" "+c+" "+d) # Muhammad Shoaib Khan Kulachi

print(a+" "+b+" "+c+" "+d+" is a student of BSCS") # Muhammad Shoaib Khan Kulachi is a student of BSCS
print(f"{a} {b} {c} {d} is a student of BSCS") # Muhammad Shoaib Khan Kulachi is a student of BSCS
print("My name is {} {} {} {}".format(a,b,c,d)) # My name is Muhammad Shoaib Khan Kulachi

# prectice set
# Q1 create a string of your name and get input from user and print its length
myName =(input("Enter your name:"))
# input function is used to take input from user
# print its length
print(len(myName)) # length of string
# print its first character
print(myName[0]) # first character of string
# print its last character
print(myName[-1]) # last character of stringMuhammad Shoaib Khan Kulachi



# part 2
# Conditionals statements in python
#  the syntax of if statement is if elif else
# if (condition):
#     statement1
# elif (condition):
#     statement2
# else:
#     statementN
# example 01
light="pink"
# light can be red, green or yellow
if light=="red":
    print("Stop")
elif light=="green":
    print("Go")
elif light=="yellow":
    print("Wait")
else:
    print("Invalid light")


# example 02
marks=float(input("Enter your marks:")) # input function is used to take input from user
# marks=int(marks) # int is used to convert string into integer
# marks can be 0 to 100
if (marks>=90 and marks<=100):
    grade="A+"
elif (marks>=80 and marks<90):
    grade="A"
elif (marks>=70 and marks<80):
    grade="B"
elif (marks>=60 and marks<70):
    grade="C"
else:
    grade="D"

print("Your grade is:",grade) # Your grade is: 

# example 03
# check whether a number is even or odd
num=int(input("Enter a number:")) # input function is used to take input from user
# num=int(num) # int is used to convert string into integer
if (num%2==0):
    print("Even number")
else:
    print("Odd number")


# example 04 
# check whether a number is positive, negative or zero
num=int(input("Enter a number:")) # input function is used to take input from user
# num=int(num) # int is used to convert string into integer
if (num>0):
    print("Positive number")
elif (num<0):
    print("Negative number")
else:
    print("Zero")


    # nested if statements
    # if (condition):
    #     if (condition):
    #         statement1
    #     else:
    #         statement2
    # else:
    #     statement3
# myAge=int(input("Enter your age:")) # input function is used to take input from user
#     # age=int(age) # int is used to convert string into integer
# if(myAge>=18):
#     print("You can Drive")
#             if(myAge>=81):
#                 print("You can Drive with a license")
#             else:
#                 print("You can not Drive with a license")
# else:
#     print("You can not Drive")


# example 05
a=int(input("Enter First number:")) # input function is used to take input from user
b=int(input("Enter Second number:")) # input function is used to take input from user
c=int(input("Enter Third number:")) # input function is used to take input from user
# find the greatest number among three numbers
if (a>b and a>c):
    print("a is greatest",a)
elif (b>a and b>c):
    print("b is greatest",b)
else:
    print("c is greatest",c)




# example 06
A=int(input("Enter First number:")) # input function is used to take input from user
B=int(input("Enter Second number:")) # input function is used to take input from user
C=int(input("Enter Third number:")) # input function is used to take input from user
D=int(input("Enter Fourth number:")) # input function is used to take input from user
# find the greatest number among four numbers
if (A>B and A>C and A>D):
    print("A is largest",A)
elif (B>A and B>C and B>D):
    print("B is largest",B)
elif (C>A and C>B and C>D):
    print("C is largest",C)
else:
    print("D is largest",D)
