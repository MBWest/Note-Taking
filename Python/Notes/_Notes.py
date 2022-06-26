#!/bin/python3

# PEP 8 is a style guide used for python3

# Help
dir(print) # Will show the help information for a function

# Print string
print("Hello, world!") # Double Quotes
print ('\n') # New Line
print('Hello, world!') # Single Quotes
print("""This string runs
multiple lines""") # Triple Quotes for Multi Lines
print("This string is " + "awesome") # Concatenate Strings

# Math

print(50 + 50) # Addition
print(50 - 50) # Subtraction
print(50 * 50) # Multiplication
print(50 / 50) # Division
print(50 ** 2) # Exponents 
print(50 % 6) # Modulo
print(50 // 6) # Division With No Leftovers

# Variables and Methods

quote = "All is fair in love and war." # Variable
print(quote.upper()) # Upper Method
print(quote.lower()) # Lower Method
print(quote.title()) # Title Method

print(len(quote)) # Print Length

# Data Types

name = "Matt" # String
age  = 30 # Integer = int(30)
gpa = 3.7 # Float = float(3.7)
var1, var2 = "neut", 4 # Assigns variables on the same line instead of on new lines
print("My name is " + name + " and I am " + str(age) + " years old!") # Use a variable inside your print function and set the data type

age +=1 # Changes the Age Variable by Adding 1
print(age)

# Functions

print("Here is an example Function!")

def who_am_i(): # This is a Function
    name = "Matt" # String
    age  = 30 # Integer = int(30)
    gpa = 3.7 # Float = float(3.7)
    print("My name is " + name + " and I am " + str(age) + " years old!")

who_am_i()

# Adding Parameters
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

# Multiple Parameters
def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y # Returns the fuction to store for later

print(multiply (7,7))
    