def check_palindrome(words):
    if len(words) <= 1:
        return True
    if words[0] != words[-1]:
        return False
    return check_palindrome(words[1:-1])

words = str(input("enter a word"))
print(check_palindrome(words))

