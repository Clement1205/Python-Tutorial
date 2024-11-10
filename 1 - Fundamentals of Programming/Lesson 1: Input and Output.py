"""
In the upcoming codes, there will be a structure for you so don't worry too much :)

# means comment, it will not be run after running process
assert x == "something"   means I assume when i run, string x will be "something". If True, nothing happens; If false,
assertion error is raised.

These messages are written in docstrings. The program will ignore these while being run.
"""

# Let's get started!

# Output
"""
There are 3 ways of printing stuff in python: printing a string, printing a variable, printing a string + a variable
1. print("bye")
2. text = "hi"
   print(text)
3. print(text + " Mimosa!")               <- this is called concatenation
"""

#Input
"""
------------------------------------------------------------------------------------------------------------------------
The same goes for requesting input from users, we store an input in a variable (we will cover this in lesson 2)
1. name = input("What is your name?")
2. user_input = input(text)
"""

# Let's try!
print('-' * 40) # a way of printing special symbols, here it's just seperating the outputs when you run so it looks better

print("bye")

text = "hi"
print(text)  # with each print, the output is automatically printed on the next line.

print(text + " Mimosa!")  # note that I added a space in front of your name, as variables do not add a space bar for you

text_with_space = " hi "
print(text_with_space + "Mimosa!") # now my new text has a space, so when i run it will automatically add a space

print('-' * 40)

user_input = input(text)
print(user_input)

name = input("What is your name? ")
print(f"Welcome home {name}!") # will teach this in lesson 2, this is a f-string, NOT a f-bomb
