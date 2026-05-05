def hex_to_decimal(hex_str):
    decimal = 0
    digits = "0123456789ABCDEF"
    for i in hex_str:
        x = digits.index(i)
        decimal = decimal * 16 + x
    return decimal

hex_str = str(input("Enter a string"))
print(hex_to_decimal(hex_str))