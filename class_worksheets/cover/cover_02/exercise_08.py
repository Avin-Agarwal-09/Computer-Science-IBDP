try:
    num = int(input("Enter an integer: "))
    print("The square is:", num ** 2)
except ValueError:
    print("Please enter a valid number.")