def decimal_to_binary(n):
    binary = ""

    while n > 0:
        i = n % 2
        binary = str(i) + binary
        n = n // 2

    return binary


n = int(input("Enter a decimal number:" ))
print(decimal_to_binary(n))