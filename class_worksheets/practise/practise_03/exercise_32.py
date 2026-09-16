def capitalize(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

user_text = input("Enter a string: ")

capitalized_string = capitalize(user_text)
print("Capitalized string:", capitalized_string)