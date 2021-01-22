import math

# Printing the list of options for the user to choose from.
print("1.Calculate the hypotenuse\n")
print("2.Calculate the sum\n")
print("3.Calculate the subtraction\n")
print("4.Calculate the multiplication\n")
print("5.Calculate the division")
# Asking the user to choose a option.
i = int(input("Choose one option from the following:\n"))
# Asking the user to enter sides of the triangle.
length_one = int(input("Enter the first side of the triangle."))
length_two = int(input("Enter the second side of the triangle."))


# Function for calculating hypotenuse of the triangle.
def calculate_hypotenuse(a, b):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    print("Hypotenuse is" + " " + str(hypotenuse))


# Function for adding the numbers.
def add(a, b):
    sum_numbers = a + b
    print("Sum is " + " " + str(sum_numbers))


# Function for subtracting the numbers.
def subtract(a, b):
    subtract_numbers = a - b
    print("Difference is " + " " + str(subtract_numbers))


# Function for multiplication of two numbers.
def multiply(a, b):
    multiply_numbers = a * b
    print("Multiplication is " + " " + str(multiply_numbers))


# Function for division of two numbers.
def div(a, b):
    if b == 0:
        print("Division by 0 not possible.")
    else:
        divide_numbers = a/b
        print("Division is " + " " + str(divide_numbers))


# Printing the output according to the option chose by the user.
if i == 1:
    calculate_hypotenuse(length_one, length_two)
elif i == 2:
    add(length_one, length_two)
elif i == 3:
    subtract(length_one, length_two)
elif i == 4:
    multiply(length_one, length_two)
elif i == 5:
    div(length_one, length_two)
else:
    print("Invalid option.Please choose between 1-5.")
