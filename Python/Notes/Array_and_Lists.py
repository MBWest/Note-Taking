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

# ----------Arrays and Lists----------

name_list = ["neut", "247CTF", "asd"] # A list with 3 items
name1, name2, name3 = name_list # Assigns a varaible name to each item in the name_list

# Defining an array (list)
my_array = ["Movies", "Games", "Python"] # A list with 3 items
"This is my first list: " + '["Movies", "Games", "Python"]'
f"You can reference a single item using an index number enclosed in []"
f"The [0] index of my_array would equate to: {my_array[0]}"

# Pulling the first and last letter of an index in a list
langs = ['C', 'C++', 'Python', 'Go', 'Java']

print(langs[2][0] + langs[2][-1] # This will produce "Pn"
      
# Delete an index from a list
del langs[0]
 
# Replace an index with a new index
langs[0] = 'Coding is fun'  # The 'C' index 

# Print each individual index of a list on a new line
for items in lang:
      print(items) 

# Add onto the end of a list (FOR EACH INDEX)
lang.extend(['Python'])  # This will add  onto the end of the list

# Add somewhere to a list
lang.append
      
# Multiply the entire list
lang * 3

# Add a list to a list
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)

# Membership testing in lists
a = ["apple", "banana", "cherry"]
'apple' in a

# Sort list
my_numbers = [1, 2, 3, 4, 5, 6, 7]
my_numbers.sort()  # Sorts my_numbers by numerical value

# Sorts lowerchase letters (Python reads upperchase and lower chase characters different)
my_letters = ['z', 'A', 'B', 'c']
my_letters.sort(key=str.lower)  # Makes all characters in my_letters lowercase then sorts them

# Sorting a list by word length
my_letters = ['z', 'A', 'B', 'c']
my_letters.sort(key=len.lower)  # Makes all characters in my_letters lowercase then sorts them by length

# Reversing a list
my_letters = ['z', 'A', 'B', 'c']
my_letters.sort(key=len, Reverse=True)  # All characters in my_letters are sorted  by length then the order is reversed