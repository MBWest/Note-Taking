#!/bin/python3

#PEP 8 is a style guide used for python3

#HELP------------------------------------------------------------

dir(print) #Will show the help information for a function

#STRINGS------------------------------------------------------------

print("Hello, world!") #Double Quotes
print ('\n') #New Line
print('Hello, world!') #Single Quotes
print("""This string runs
multiple lines""") #Triple Quotes for Multi Lines
print("This string is " + "awesome") #Concatenate Strings

#MATH------------------------------------------------------------

print(50 + 50) #Addition
print(50 - 50) #Subtraction
print(50 * 50) #Multiplication
print(50 / 50) #Division with remainder (or a float)
print(50 ** 2) #Exponents 
print(50 % 6) #Modulo - Takes what is left over
print(50 // 6) #Division with no remainder

#VARIABLES AND METHODS------------------------------------------------------------

quote = "All is fair in love and war." #Variable
print(quote.upper()) #Upper Method
print(quote.lower()) #Lower Method
print(quote.title()) #Title Method

print(len(quote)) #Print Length

#DATA TYPES------------------------------------------------------------

name = "Matt" #String
age  = 30 #Integer = int(30)
gpa = 3.7 #Float = float(3.7)
var1, var2 = "neut", 4 #Assigns variables on the same line instead of on new lines
print("My name is " + name + " and I am " + str(age) + " years old!") #Use a variable inside your print function and set the data type

age +=1 #Changes the Age Variable by Adding 1
print(age)

#FUCNTIONS------------------------------------------------------------

print("Here is an example Function!")

def who_am_i(): #This is a Function
    name = "Matt" #String
    age  = 30 #Integer = int(30)
    gpa = 3.7 #Float = float(3.7)
    print("My name is " + name + " and I am " + str(age) + " years old!")

who_am_i()

#Adding Parameters
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100) #Call function, with provided argument (100)

#Multiple Parameters
def add(x,y):
    print(x + y)

add(7,7)#Call function, with provided argument (7,7)

def multiply(x,y):
    return x * y #Returns the fuction to store for later

print(multiply (7,7)) #Call function, with provided argument (7,7)

#BOOLEAN EXPRESSIONS (TRUE OR FALSE)------------------------------------------------------------

bool1 = True #Boolean expression = True
bool2 = 3*3 == 9 #Boolean expression = True
bool3 = False #Boolean expression = False
bool4 = 3*3 != 9 #Boolean expression = False

print(bool1,bool2,bool3,bool4) #Print the bool1-4 variables
print(type(bool1)) #Print the type of item that bool1 is

bool5 = "True" #Quotes make this a string and not a boolean
print(type(bool5)) #Print the type of item that bool5 is

#RELATIONAL AND BOOLEAN OPERATORS------------------------------------------------------------

greater_than = 7 > 5 #True
less_than = 5 < 7 #True
greater_than_equal_to = 7 >= 7 #True
less_than_equal_to = 7 <= 7 #True

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

print(test_and, test_and2, test_or, test_or2)

