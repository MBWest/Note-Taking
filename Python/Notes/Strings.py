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