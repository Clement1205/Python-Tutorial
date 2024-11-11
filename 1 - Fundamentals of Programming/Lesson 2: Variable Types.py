"""
There are 5 commonly used data types in all programming languages,
Integer (int): only exact numbers (no decimals or fractions)
Float (float): contains all numbers including integers
Boolean (bool): True or False
String (str): "This is a string"
Lists, Tuples: ["will be covered later!"], ()

Casting:
your_age = 20
str(your_age) casts the number 20 into string (to print it out)
int("20") converts the string "20" into an integer for calculation
age = int(input("Please enter your age: ")) stores the user input as an integer. Error will occur if the input is NOT an
integer.
"""

# Let's try!
integer = 10 # This is called initialisation. You need to store a value into a variable before using it.
float = 10.2 # do not recommend you creating names like this or similar to operators, this is just for your understanding.
boolean = True # strongly recommend making meaningful names like absent = True, exam_passed = False.
string = "hi" 

print(integer + float)
print(boolean)
print(string + "\n")

print(f"{string}! This is a mixture of variables and strings that I type")
print(string + "! This is a mixture of variables and strings that I type")

# The format of f-strings are f"", everything you write inside is a string. To add a variable, simply add a {}.
print('-' * 40)

# Advanced Concepts
# Converting integer into float
print(f"{integer:.2f}") # 2 decimal places

print(f"The price is {integer * float} dollars")

