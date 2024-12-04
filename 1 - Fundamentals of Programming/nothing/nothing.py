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