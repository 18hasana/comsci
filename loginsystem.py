username = "AdamHasan"
password = "C0mpl3x!"
attempts = 3

print("Welcome to the login page")


while attempts > 0:
    usernameInput = input("\nPlease enter your username: ")
    passwordInput = input("\nPlease enter your password: ")
    
    if usernameInput != username:
        print("\nIncorrect Username")
    elif passwordInput != password:
        print("\nIncorrect Password")
    else:
        print(f"\nYou are logged in as {username}")
        break
    
    attempts -= 1

    print(f"\nYou now have {attempts} attempt(s) left")
