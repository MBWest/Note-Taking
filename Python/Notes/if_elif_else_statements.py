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