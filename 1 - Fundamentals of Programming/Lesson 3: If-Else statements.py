"""
if-else statements work similarly like normal life logic. 
If you study, then you will have good grades. If not (else), you will
send your grades to Jesus.

if-statement operators:

Note: Indentations are SUPER IMPORTANT in python!
"""

# Let's try!
# 1.
age = input("Please enter your age: ")
if age > 0 and age < 18: # (age > 0 and age < 18) is a parameter. If it is true, the indented statement will be printed
    print("Hello kiddo!")
elif age >= 18 and age <= 100: # elif means else if. if the first parameter is false, it will come here
    print("Hello adult!")
else:  # age must be between 1 to 100 (you need to think of the boundaries and think of the constraints)
    print("You are faking your age!")

print('-' * 40)
# 2.
functional = True # True when an app is functional, False when the app is not
if functional != True or functional == False: # this is just an illustration, both mean the same thing
    print("Maintenance is needed.")

# no need to write "else:" if you want it to print nothing
print('-' * 40)
# 3.
first_no = input("Please enter the first number: ")
second_no = input("Please enter the second number: ")
if first_no > second_no:
    print(f"{first_no} is larger than {second_no}.")
elif first_no < second_no:
    print(f"{first_no} is smaller than {second_no}.")
elif first_no == second_no:
    print(f"{first_no} is equal to {second_no}.")
else:
    print("Please enter a number.")

print('-' * 40)
# Advanced Concepts
# 4.
username = input("Please enter your username: ")
if username.lower() == "mimosa": #lower() turns every alphabet in the string into lowercase; upper() for uppercase
    print("Access Granted.")
else:
    print("Access Denied.")