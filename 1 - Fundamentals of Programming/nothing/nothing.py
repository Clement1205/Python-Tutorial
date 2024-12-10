def text():
    text = "mimosa" #string
    print(len(text))

    text_list = ["mimosa"] #list
    print(len(text_list))

    text_list1 = ("mimosa", "hi") #tuple
    print(len(text_list1))
    

    return "done", "Done"

text1, text2 = text()
print(text1)
print(text2)

for i in range(1, 100):
    if i == 2:
        break
    print(i)

i = 1
if i < 0 | i > 0:
    print(i)



print('-' * 40)
def something(n):
    container = 0
    while(True):
        if n // 2 == 1:
            return (container + 1)
        else:
            if n % 2 == 1:
                container += 1
                n /= 2
            else:
                n /= 2

print(something(5))
print(something(7))
print(something(8))