"""
A CSV file is like a table with rows and columns. Each data is stored in commas, seperated by new lines.
(see example.csv)

You will only read and write a csv file. 
For reading, you want to extract the values from the csv file and mess with the data.
For writing, you want to write the values to a csv file.

Type 'cd 2\ -\ Data\ Analytics\ of\ Python/' in the terminal before running the code!
"""
output_data = []

with open("example.csv", "r") as infile:
    next(infile) # skip the first row (ID,Name,Math,Science,History)
    for line in infile:
        data = line.strip().split(",") # strip removes extra space bars, split ',' changes from 'a, b, c' to 'a','b','c'
        id = data[0]
        name = data[1] # you don't have to add this everytime, just add it when you wanna use the values
        math = float(data[2]) #data[2] refers to the maths column in example.csv, this extracts the math score from every 
        science = float(data[3]) #                                                                                   line
        history = float(data[4])
        average = ((math + science + history) / 3)
        output_data.append((id, name, average))

with open("example_out.csv", "w") as outfile:
    outfile.write("ID, Name, Average")
    for id, name, average in output_data: # as long as these 3 are in output_data list, then do the following statement
        outfile.write(f"{id},{name},{average:.1f}\n")