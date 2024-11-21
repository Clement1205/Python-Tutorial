"""
My own definition of functions is that it helps you group your codes together. I seperate my code into parts and call them
from underneath.

Note:
1. In every function, you have to return something out, no matter a value or a string. If not, add a word "pass"

2. The brackets next to the function name are called parameters. You have to fulfill those parameters when you call the
function from underneath. E.g def function_name(num1, num2) blablabla, when you call it, function_name(20, 50)

3. The functions must be ABOVE your codes that are calling the function, or your codes cannot find the function and have
an error.
"""
# num1 and num2 are called local variables. They are only available within a function because they are created within a
# function

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2): 
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def text():
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")
    return num1, num2

functional = True
while(functional == True):
    values = [1, 2, 3, 4, "exit"] # set a list of inputs, if the user are not inputting these, they have to input again

    print('*' * 40)
    print("Welcome to Calculator! Please choose one of the options below:\n")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("exit - Exit")
    option = input("Your option: ")

    # lower() makes everything lowercase, strip() removes all spaces in the beginning and the end of strings
    match option.lower().strip() in values: 
        case 1:
            num1, num2 = text()
            addition(num1, num2)
        case 2:
            num1, num2 = text()
            subtraction(num1, num2)
        case 3:
            num1, num2 = text()
            multiplication(num1, num2)
        case 4:
            num1, num2 = text()
            division(num1, num2)
        case "exit":
            print("Thank you for using Calculator!")
            functional == False
            break
        case _:
            print("Option not available. Please try again.")
            continue