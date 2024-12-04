"""
There are 3 types of iterations: do-while, while loops, and for loops. They all work similarly, but most people use for or
while loops. Here are their differences:

1. do-while: you do that code first before looping (repeating) it based on the conditions you've written.
2. while loops: you loop it based on the conditions you've written.
3. for loops: another type of while loop, but can more conveniently iterate between lists or even dataframes.

Break means breaking the loop, continue means skipping the current loop to the next one.

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

for i in range(1, 21):
    if i % 2 == 0:
        continue
    elif i > 15:
        print("Break!\n")
        break
    else:
        print(i, end= " ")

print("\n" + "-" * 40)
course = "Computer Science"

for ch in course :
	print(ch) # can you guess the output?
