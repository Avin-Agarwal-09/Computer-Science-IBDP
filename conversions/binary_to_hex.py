def binary_to_hex(binary_str):
    while len(binary_str) % 4 != 0:
        binary_str = "0" + binary_str
    
    digits = "0123456789ABCDEF"
    hex_str = ""
    
    for i in range(0,len(binary_str),4):
        temp_bundle = binary_str[i:i+4]
        value = 0
        for j in temp_bundle:
            value = value * 2 + int(j)
        hex_str = hex_str + digits[value]

    return hex_str

binary_str = str(input("Enter a binary string: "))
print(binary_to_hex(binary_str))