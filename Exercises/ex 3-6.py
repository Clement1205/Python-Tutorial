# Predefined credentials
correct_username = "user123"
correct_password = "password456"
two_factor_enabled = True
correct_2fa_code = "7890"

# Ask user for their username, password, and two-factor authentication code (if enabled)
username = input("Enter your username: ")
password = input("Enter your password: ")

# Conditional block for login authentication
if ():
    if ():
        two_factor_code = input("Enter the 2FA code sent to your device: ")
        if ():
            print("Login successful! Welcome!")
        else:
            print("Invalid two-factor authentication code. Access denied.")
    else:
        print("Login successful! Welcome!")
else:
    print("Invalid username or password. Access denied.")
