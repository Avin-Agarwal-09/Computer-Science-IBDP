def decimal_to_binary(n):
    binary = ""

    while n > 0:
        i = n % 2
        binary = str(i) + binary
        n = n // 2

    return binary

def hex_to_binary(hex_str):
    digits = "0123456789ABCDEF"
    binary_str = ""

    for i in hex_str: #hex to decimal
        value = 0
        for j in range(len(digits)):
            if digits[j] == i:
                value = j
                binary_value = decimal_to_binary(value)
                binary_str += binary_value

    return binary_str

hex_str = str(input('Enter a string: '))
print(hex_to_binary(hex_str))
        