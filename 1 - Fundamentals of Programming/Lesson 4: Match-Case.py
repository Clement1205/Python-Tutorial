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


# Super Advanced Concept (can ignore if your course did not teach stuff like this)
print('-' * 40)
sensor_data = [
    ("temperature", 75.0),
    ("humidity", 55),
    ("pressure", 1015),
    ("temperature", 100.0),  # Too hot!
    ("humidity", 25),         # Too low!
    ("pressure", 990),        # Too low!
]

# Process each tuple in the sensor_data list
for data in sensor_data:
    match data:
        case ("temperature", temp): # follow the structure in the list!
            if temp > 90:
                print(f"Warning! High temperature detected: {temp}°C")
            else:
                print(f"Temperature is normal: {temp}°C")
        
        case ("humidity", hum):
            if hum < 30:
                print(f"Low humidity level detected: {hum}%")
            else:
                print(f"Humidity level is normal: {hum}%")
        
        case ("pressure", pres):
            if pres < 1000:
                print(f"Low pressure detected: {pres} hPa")
            else:
                print(f"Pressure level is normal: {pres} hPa")
        
        case _:
            print("Unknown sensor data")

print('-' * 40)
# test for data types
def handle_input(user_input):
    match user_input:
        case int():
            print(f"Integer received: {user_input}")
        case str():
            print(f"String received: {user_input}")
        case list() if len(user_input) > 0:
            print(f"List received with {len(user_input)} elements")
        case _:
            print("Unknown input type")

# Example usage
handle_input(10)                # Output: Integer received: 10
handle_input("Hello")           # Output: String received: Hello
handle_input([1, 2, 3])         # Output: List received with 3 elements