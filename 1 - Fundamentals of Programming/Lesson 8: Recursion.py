"""
Recursion is just another type of for loop, but in a function. This only works when you want to loop the ENTIRE function,
not just a few lines of code inside the function.

You must include a way to stop the recursion or the code will loop it forever! The most common way is to start from a base
case, e.g break the loop if num = 1
"""

def addition(num):
    if num == 0:
        return num
    elif num > 0:
        return num + addition(num-1) # this loops the function till num = 0, then it will return num (when it is 0), num
    elif num < 0:  #                                                                           (when it is 1), and so on
        return num + addition(num+1)
    
num = input("Please enter a number: ")
print(addition(float(num)))

# if num = 5,
# num is > 0, so it will return 5 + addition(5-1)
# in addition(5-1), num = 4, which is still > 0, so it will return 5 + 4 + addition(4-1)
# blablabla
# in addition(1-1), num = 0, so it will return num, which is 0.
# so in the end we go back to the addition(5), the equation will be 5 + 4 + 3 + 2 + 1 + 0 = 15
