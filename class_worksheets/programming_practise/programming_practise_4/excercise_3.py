def mix_string(string1, string2):
    first_char = string1[0] + string2[0]
    middle_char = string1[int(len(string1) / 2):int(len(string1) / 2) + 1] + string2[int(len(string2) / 2):int(len(string2) / 2) + 1]
    last_char = string1[len(string1) - 1] + string2[len(string2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)
string1 = str(input("Enter first string: "))
string2 = str(input("Enter second string: "))
mix_string(string1, string2)