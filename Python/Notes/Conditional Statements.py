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

# ----------if, elif, else statements----------
# if, elif, else statements
check = False

if check is False:
    print("It is false")
elif check is True:
    print("It is True")

# For/while loops (FOR each item, WHILE condition exists)
numbers = [1, 2, 3, 4, 5]

for items in numbers:
    print(items)

# Another example of for loop

names = ["Nick", "Bob", "John", "Matthew"]

for items in names:
    print("This persons name is", items)

# While loop example
run = True
current = 1

while run:
    if current == 10:  # If current is equal to 10 set run to False until then do the else statement
        run = False

    else:
        print(current)
        current += 1