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
sports = ["bowling", "badminton", "table tennis"]
print(sports)

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