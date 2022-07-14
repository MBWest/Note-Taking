#!/bin/python3

#PEP 8 is a style guide used for python3

#IMPORTING------------------------------------------------------------

import sys #System functions and parameters

from datetime import datetime as dt #Import a function from a module while refering to it with an alias

print(sys.version)
print(dt.now())

#HELP------------------------------------------------------------

dir(print) #Will show the help information for a function

#STRINGS------------------------------------------------------------

print("Hello, world!") #Double Quotes
print ('\n') #New Line
print('Hello, world!') #Single Quotes
print("""This string runs
multiple lines""") #Triple Quotes for Multi Lines
print("This string is " + "awesome") #Concatenate Strings

#ADVANCED STRINGS, IMUTABLE------------------------------------------------------------

my_name = 'Matt'

print(my_name[0]) #First letter
print(my_name[-1]) #Last letter
sentence = "This is a sentence."
print(sentence[:4]) #Print 'This'
print(sentence.split()) #Delimeter - Defeault is a space
print(sentence.split()[:1])

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'" #Use different quotes if you need to have a quote inside quotes
print(quote)
quote = "He said, \"give me all your money\"" #Character escaping with \
print(quote)

too_much_space = "                                hello      "
print(too_much_space.strip()) #Strip out extra space

print("A" in "Apple") #True
print("a" in "Apple") #False

letter = "A"
word = "Apple"

print(letter.lower() in word.lower()) #Improved

movie = "The Hangover"

print("My favorite movie is {}.".format(movie)) #String Format Method

print("My favorite movie is %s." %movie) #Percent String

print(f"My favorite movie is {movie}.") #String Literal
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
test_not = (7 > 5 ) or ( 5 > 7) # False
print(test_and, test_and2, test_or, test_or2, test_not)

#CONDITIONAL STATEMENTS------------------------------------------------------------

#Example 1
def drink(money):
    if money >= 2:
        return "You have got yourself a drink!"
    else:
        return "No drink for you!"

print(drink(1))
print(drink(3))

#Example 2
def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We are getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money"
    elif (age < 21) and (money >= 5):
        return "Nice try guy!"
    elif (age < 21) and (money < 5):
        return "You are too young and too poor!"

print(alcohol(21,6))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

#LISTS - MUTABLE [0,1,2,3,...]------------------------------------------------------------

movies = ["When Harry Met SAlly", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #Returns the second item in the list
print(movies[0]) #Returns the first item in the list
print(movies[1:3]) #Returns the first index number given right until the last number, but not include the last number
print(movies[1:]) #Returns the first index through the rest of the list
print(movies[:1]) #Returns only the items before the first index
print(movies[-1]) #Returns last item in list

print(len(movies)) #Print length of movies list

movies.append("JAWS") #Appends to the end of the list

print(movies[-1])  #Returns last item in list

movies.insert(2,"Hustle") #Insert Hustle into index 2 of the List

movies.pop() #Removes the last item in the movies list
movies.pop(0) #Removes the first item in the movies list
print(movies) #Prints the movie list

amber_movies = ['Just Go With It', '50 First Dates'] 

our_favorite_movies = movies + amber_movies

print(our_favorite_movies)

grades = [['bob', 82], ['Alice', 90], ['Jeff', 90]]

bob_grades = grades[0][1] #Display Bobs grades
print(bob_grades) #Print Bobs grades
grades[0][1] = 83 #Change bobs grade
print(grades) #Print grades

#TUPLES - NOT MUTABLE, (a, b, c, d...)------------------------------------------------------------

grades = ("a", "b", "c", "d", "f")

grades.pop()

#DICTIONARIES - KEY/VALUE PAIRS {}------------------------------------------------------------

drinks = {"White Russian": 7, "Old Fassion": 10, "Lemon Drop": 8} #Drink is the key, price is the value

print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy JR.", "Mort"]}

print(employees)

employees['Legal'] = ["Mr. Frond"] #Adds new key/value pair

print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #Adds new key/value pair

print(employees)

drinks["White Russian"] = 8

print(drinks.get("White Russian")) #Print the Value of the "White Russian"
#LOOPING------------------------------------------------------------

#FOR LOOP - Start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)

#WHILE LOOP - Execute as long as TRUE
i = 1
while i <= 10:
    print(i)
    i += 1

#SOCKETS------------------------------------------------------------

import socket
HOST = '127.0.0.1' #af_inet
PORT = 7777 #sock_stream

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is IPv4, sock_stream is a port

s.connect((HOST,PORT))

