username = "AdamHasan"
password = "C0mpl3x!"
attempts = 3

print("Welcome to the login page")


while attempts > 0:
    usernameInput = input("\nPlease enter your username: ")
    passwordInput = input("\nPlease enter your password: ")
    
    if (usernameInput == username) and (passwordInput != password):
        print("\nyou have forgotten the password")
    elif (usernameInput != username) and (passwordInput != password):
        print("\naccess denied")
    elif (usernameInput == username) and (passwordInput == password):
        print(f"\naccess granted")
        break
    
    attempts -= 1

    print(f"\nYou now have {attempts} attempt(s) left")
