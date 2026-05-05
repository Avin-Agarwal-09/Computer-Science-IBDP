def set_password():
    correct = False
    password = "" 
    
    while not correct:
        password = input("Please enter a password that is atleast eight characters long with no consecutive repeated characters: ")

        if len(password) < 8:
            print("Password is too short, try again")
        
        repeats = False
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                repeats = True
                break

        if repeats == True:
            print("Password has repeated characters, try again")
            continue

        tries = 0
        while tries < 3:
            double_check = input("Please re-enter your password")
            if password == double_check:
                print("Your password is accepted")
                return

            else:
                tries += 1
                if tries < 3:
                    print("passwords dont match, try again")
                else:
                    print("too many fails, restart")

set_password()
