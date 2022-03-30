# ----------Arrays and Lists----------
# Defining an array (list)
my_array = ["Movies", "Games", "Python"]
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