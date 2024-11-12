"""
Match-Case statements are very similar to If-Else statements, it expresses clearer in situations when there are lots of if
statements.
"""

# Let's try!
print("Welcome to Calculator! Please choose one of the options:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
option = input("Please choose an option: ")

match option:
    case "1": # need double quotation marks because option variable is a STRING, not an integer.
        print("You chose addition.")
    case "2":
        print("You chose subtraction.")
    case "3":
        print("You chose multiplication.")
    case "4":
        print("You chose division.")
    case _:
        print("Invalid option.")