def decimal_to_hex(n):
    digits = "0123456789ABCDEF"
    hex_str = "" 
    while n > 0:
        x = n % 16
        hex_str = digits[x] + hex_str
        n = n // 16
    return hex_str

n = int(input("Enter a decimal value: "))
print(decimal_to_hex(n))