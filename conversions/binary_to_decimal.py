#Convert binary to decimal

def binary_to_decimal(binary_str):
    value = 0
    exponent = len(binary_str)-1

    for i in binary_str:
        value = value + int(i)*(2**exponent)
        exponent = exponent - 1
    
    return value

binary_str = str(input("Enter a binary string: "))
print(binary_to_decimal(binary_str))

