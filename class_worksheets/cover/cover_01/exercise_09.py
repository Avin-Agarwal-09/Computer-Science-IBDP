correct_pin = 1234
attempts = 0
while attempts < 3:
    try:
        pin = int(input("Enter your 4-digit PIN: "))
        if pin == correct_pin:
            print("Access Granted")
            break
        else:
            print("Incorrect PIN. Try again.")
            attempts = attempts + 1
    except:
        print("Invalid input. Please enter numbers only.")
        attempts = attempts + 1

if attempts == 3:
    print("Account Locked.")
