"""
There are 3 types of iterations: do-while, while loops, and for loops. They all work similarly, but most people use for or
while loops. Here are their differences:

1. do-while: you do that code first before looping (repeating) it based on the conditions you've written.
2. while loops: you loop it based on the conditions you've written.
3. for loops: another type of while loop, but can more conveniently iterate between lists or even dataframes.

NOTE: There are NO do-while loops in python! Only for loops and while loops are available.
"""
# Let's try!
print("-" * 40)
temp = 1
print("while loop: ", end= " ") # after you finish printing 1 line, the ending is " " instead of \n
while(temp <= 10):
    print(temp, end= " ") 
    temp += 1 # the same as temp = temp + 1

# for loop
print("\nfor loop: ", end= " ")
for i in range(1, 11): # for loop in range (1, x) prints out from 1 to (x-1)
    print(i, end= " ")

print("\n" + "-" * 40)
# Advanced Concepts
# using for loops in lists (this method is only available in python!)
marks = [10, 90, 77, 78, 45, 29, 71, 62, 88, 50]
sum = 0

for i in marks:   # this iterates the list from the beginning to the end, storing the value in i for each iteration.
    print(i, end= " ")     # for each iteration, I print the value of i out, seperated with a space
    sum += i
average = sum / len(marks) # len() is only available for lists (count no. of values) and strings (count no. of characters)

print(f"Average: {int(average)}") # casting average into integer (same as round down!)

