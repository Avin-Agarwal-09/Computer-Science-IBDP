def validate_user_input(age, email, phone):
    try:
        age = int(age)
        if age < 0 or age > 150:
            print("Invalid age: must be between 0 and 150.")
            return
    except:
        print("Invalid age: must be a number.")
        return

    if "@" not in email or "." not in email:
        print("Invalid email: must contain '@' and '.'.")
        return

    if not phone.isdigit():
        print("Invalid phone: must contain only numbers.")
        return

    if len(phone) != 10:
        print("Invalid phone: must be exactly 10 digits.")
        return

    print("All inputs are valid!")
