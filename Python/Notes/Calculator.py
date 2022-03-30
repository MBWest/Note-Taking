# -----Building a Calculator one way-----
# Define functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Take input from the user
print("Our Magic Calculator\nSelect operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter choice (1,2,3,4):")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")

# -----Building a Calculator another way-----
print("Our Magical Calculator\nType 'quit' to exit\n")
previous = 0
run = True


def perform_math():
    global run  # Allow this function to access the 'run' variable
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:() ]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()

