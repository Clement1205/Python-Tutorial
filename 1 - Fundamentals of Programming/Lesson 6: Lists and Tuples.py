"""
There are 4 ways of storing data. There are lists, tuples, sets and dictionaries! Here are their differences:

1. Lists []: store every variable in a [], modifiable
2. Tuples (): store every variable in a (), unmodifiable
3. sets {}: store every variable in a {}, modifiable, unordered (cannot access it using name[0])
4. dictionaries {}: use key value pairs to link to data, modifiable, no duplicates allowed
-------------------------------------------------------------------------------------------------------------------------
Built in list-functions:
1. append(item): adds an element at the end of the list 
2. insert(index, item): adds an element at the specified position
3. pop(index): removes the element at the specified position
4. pop(): removes the last element
5. remove(item): removes the item with specified value
6. index(item): returns the index of the first element with the specified value
7. clear(): removes all elements from the list
8. reverse(): reverses the order of the list
9. sort(): sorts the items in the list alphabetically (does NOT work for numbers)
-------------------------------------------------------------------------------------------------------------------------
"""
# For example
sports = ["bowling", "table tennis", "badminton"]
print(sports)

sports.sort()
print(f"Sort: {sports}")

sports.append("volleyball")
print(f"Append: {sports}") # concatenation does NOT work for lists!

"""
An index refers to the position of the element in the array.
All indices in arrays start from 0 and adds up.
In sports array, the index of "bowling" is 0, "badminton" is 1, and so on. You can use this to iterate through lists in a
for loop, but python has an easier way.
"""
sports.pop(2)
print(f"Pop(2): {sports}")

sports.pop()
print(f"Pop(): {sports}")

sports.remove("badminton")
print(f"Remove: {sports}")

sports.insert(1, "football")
print(f"Insert(): {sports}")

sport1 = sports
print(sport1)

"""
You can use for loops to iterate through lists!
"""
# using for loops in lists (this method is only available in python!)
marks = [10, 90, 77, 78, 45, 29, 71, 62, 88, 50]
sum = 0

for i in marks:   # this iterates the list from the beginning to the end, storing the value in i for each iteration.
    print(i, end= " ")     # for each iteration, I print the value of i out, seperated with a space
    sum += i
average = sum / len(marks) # len() is only available for lists (count no. of values) and strings (count no. of characters)

print(f"\nAverage: {int(average)}") # casting average into integer (same as round down!)

"""
Tuples are just the same as lists, except it is UNmodifible. You cannot edit anything inside, the elements inside are
fixed when created. Any attempt to try to modify tuples will result in an error.
"""
marks_tuple = tuple(marks)
print(marks_tuple)

"""
-------------------------------------------------------------------------------------------------------------------------
Some extra list and tuple expressions:
1. list[index]: returns the element of the list based on the index number
2. list[-index]: count the index from the right, and return the element on the list based on the number
3. list[index:]: returns everything after the index number (INCLUDING the index element!)
4. list[::index]: returns the first element, (first+index) element, (first+index+index) element, etc
5. list[num::index]: returns the num element, (num+index) element, (num+index+index) element, etc
6. list[::-1]: returns the list in descending order (from the right to left)
7. max(list): returns the element with the largest index in the list (the rightmost one)
8. min(list): returns the element with the smallest index in the list (the leftmost one)
-------------------------------------------------------------------------------------------------------------------------
"""
print('-' *40)
t1 = ("apple", "box", "cake", "disk")
t2 = (1, 2, 3, 4, 5)

print(f"t1[3] = {t1[3]}")
print(f"t1[-2] = {t1[-2]}")
print(f"t1[2:] = {t1[2:]}")
print(f"t1[::2] = {t1[::2]}")
print(f"t1[1::2] = {t1[1::2]}")
print(f"t1[-1] = {t1[-1]}")
print(f"max(t1) = {max(t1)}")
print(f"min(t1) = {min(t1)}")

"""
-------------------------------------------------------------------------------------------------------------------------
Built-in dict expressions:
1. clear(): removes all elements from the dictionary
2. get(key): returns the value of a specified key
3. items(): returns a list containing a tuple for each key value pair
4. keys(): returns a list containing the dictionary's keys
5. pop(key): removes the element with the specified key
6. values(): returns the list with all the values in the dictionary
-------------------------------------------------------------------------------------------------------------------------
"""
capital = {
  "UK": "London", 
  "US": "Washington DC", 
  "China": "Beijing",
  "Japan": "Tokyo"
} # UK is the key, London is the value, that's why dictionaries are key value pairs

# loop through the dict extracting key and value

for c,r in capital.items():
    print( c,r ) # c and r only works within the for loop




# Advanced Concept: Enumerate
print('-' *40)
for ele in enumerate(t1):
    print (ele)

# unpacking the tuple (index, value) into the variables index and value, so you are printing the value -> no brackets
for index, value in enumerate(t1):
    print(index, value)

# changing index and printing separately
for count, ele in enumerate(t1, 100):
    print (count, ele)

# getting desired output from tuple
for count, ele in enumerate(t1):
    print(count)
    print(ele)