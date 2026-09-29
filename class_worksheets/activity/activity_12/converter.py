def binary_to_decimal(binary_str):
    value = 0
    exponent = len(binary_str) - 1
    for digit in binary_str:
        value += int(digit) * (2 ** exponent)
        exponent -= 1
    return value

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary