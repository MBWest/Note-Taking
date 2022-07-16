#STRINGS, IMUTABLE------------------------------------------------------------

print("Hello, world!") #Double Quotes
print ('\n') #New Line
print('Hello, world!') #Single Quotes
print("""This string runs
multiple lines""") #Triple Quotes for Multi Lines
print("This string is " + "awesome") #Concatenate Strings
print("\\ \x41\x42\x43") #This will print hex
print('a' * 10) #Prints 'a 10 times

my_name = 'Matt'

print(my_name.startswith("M")) #Returns true
print(my_name.index("Matt")) #Prints the index of 'Matt'
print(my_name.lower()) #Prints my_name in all lowercase 
print(my_name.upper()) #Prints my_name in all uppercase

print(my_name.encode("utf-8")) #Encode a string
print(my_name.rjust(25)) #Right justify the string with " "
print(my_name.rjust(25, "X")) #Right justify the string with "X"
print(my_name.ljust(25, "X")) #Left justify the string with "X"


print(my_name[0]) #First letter
print(my_name[-1]) #Last letter

sentence = "This is a sentence."
print(sentence.replace(".", "!")) #Replace the . with a !
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

print("My favorite movie is %s." %movie) #String replace (d,x,f are other uses)

print(f"My favorite movie is {movie}.") #String Literal

string = "I am a string!"

length = len(string)

print(f"string is {length:.3f} characters long") #Print the length as a float (14.000)

print(f"string is {length:x} characters long") #Print the length as hex (e)

print(f"string is {length:b} characters long") #Print the length as binary (1110)

print(f"string is {length:o} characters long") #Print the length as octal (16)