def remove_characters(string, n):
    if n >= len(string):
        return ""
    else:
        return string[n:]

string = input("Enter a string: ")
n = int(input("Enter number of characters to remove: "))
newstring = remove_characters(string, n)
print(newstring)