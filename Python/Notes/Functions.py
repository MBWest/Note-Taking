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

# ----------Built in Functions----------
# Built in functions (Print, str, int, float, bool, len, sorted)
print("Print things to the console")  # Print things to the console
str(5)  # Convert anything to a string
int(5)  # Convert a number to an integer
float(5.5)  # Convert a number to a floating decimal point number
bool("True")  # Convert strings to a boolean
len("Hello")  # Find the length of a string
len([1, 2, 3, 4, 5])  # Find the number of item in an array
min(1,2,3)  # Smallest number
max(1,2,3)  # Largest number
max(("horse", "Pig", "cow"), key=len)  # Finds the longest length word
list(reverse(mylist)) # Returns mylist in reverse order
__reversed__()  # Supports the sequence method. You can use range
a_new_array = [1, 8, 45, 23, 99, 65, 102]
print(sorted(a_new_array))  # Sort an array into numerical order
a_string_array = ["a", "B", "c", "D"]
print(sorted(a_string_array))  # Sort an array in alphabetical order (Numbers > Upper > Lower)
isistance(object, classinfo)  # Returns a True or False. Example, isistance("string", str), isistance("string", (str, int)) # works like an or
enumerate(iterable) # Enumerate a iterable object
f = open(file, mode=*)  # Append a file. Must save open file as a variable first. mode=r is read

# ----------Functions----------
# Defining a function (use_snake_case)
def my_function():
    print("This is my function.")
    print("A second string.")

# Call a function
my_function()

# Adding arguments to a function
def my_second_function(str1, str2):  # Functions belong in the ()
    print(str1)
    print(str2)

my_second_function("This is argument1.", "This is the second argument which is also a string.")  # Call the function and use the arguments that were inputted 
my_second_function("Hello ", "World!")   # Call the function and use the arguments that were inputted

# Default arguments in functions
def print_something(name="Someone", age="Unknown"):  # You can set default arguments to be used in case you do not pass it a value
    print("My name is", name, "and my age is", age)  # You can use comma's (,) or wrap the int in a str()

print_something("Matthew", str(29))

# Keyword arguments
def print_something_again(name="Someone", age="Unknown"):  # You can set default arguments to be used in case you do not pass it a value
    print("My name is", name, "and my age is", age)  # You can use comma's (,) or wrap the int in a str()

print_something_again(age=str(29), name="Matt")

# Infinite arguments
def print_people(*people):  # Create an array that prints out peoples names
   for person in people:
        print("This person is", person)


print_people("Matthew", "Nick", "Jack", "King", "Smiley")

# Return values (Return a value to do something else with it)
def do_math(num1, num2):  # Defining a function named do math with 2 functions
    return num1 + num2  # We are adding the function num1 and num2

math1 = do_math(5, 7)
math2 = do_math(11, 34)

print(f"First sum is: {math1} and the second sum is {math2}!")

# ----------Comparators----------
equal_to = "=="
not_equal_to = "!="
less_than = "<"
greater_than = ">"
less_than_or_equals_to = "<="
greater_than_or_equals_to = ">="

# ----------Formating Functions----------
"Hello there {}.".Format("Matthew")
"R{0}-D{0}".Format(2)