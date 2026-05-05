def numbers(text):
    for char in text:
        if '0' <= char <= '9':
            return True
    return False
string = input("Enter a string: ")
if numbers(string):
    print("contains a number")
else:
    print("does not contain a number")