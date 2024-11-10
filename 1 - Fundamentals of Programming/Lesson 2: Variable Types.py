"""
There are 5 commonly used data types in all programming languages,
Integer (int): only exact numbers (no decimals or fractions)
Float (float): contains all numbers including integers
Boolean (bool): True or False
String (string): "This is a string"
Lists, Tuples: ["will be covered later!"], ()
"""

integer = 10 # This is called initialisation. You need to store a value into a variable before using it.
float = 10.2 # do not recommend you creating names like this or similar to operators, this is just for your understanding.
boolean = True # strongly recommend making meaningful names like absent = True, exam_passed = False.
string = "hi" 

print(integer + float)
print(boolean)
print(string)

print(f"{string}! This is a mixture of variables and strings that I type")
print(string + "! This is a mixture of variables and strings that I type")

# The format of f-strings are f"", everything you write inside is a string. To add a variable, simply add a {}.