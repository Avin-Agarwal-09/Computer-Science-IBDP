name = str(input("What is your name?"))
gender = str(input("What is your gender?"))
age = int(input("What is your age?"))
if gender == "Male":
    if age >= 65:
        print("you can retire ")
    else:
        print("you can not retire, wait ", 65-age, "more years")
else:
    if age >= 62:
        print("You can retire ")
    else:
        print("you can not retire, wait ", 62-age, "more years")
