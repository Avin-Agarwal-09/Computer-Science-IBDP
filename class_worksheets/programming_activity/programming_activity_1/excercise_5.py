def convert_decimal(decimal_num):
    if not isinstance(decimal_num, int):
        raise TypeError("Input must be an integer.")
    if decimal_num < 0:
        print("Conversion for negative numbers using built-in functions might have '0b-', '0o-', '0x-' prefixes.")

    binary_representation = bin(decimal_num)
    octal_representation = oct(decimal_num)
    hexadecimal_representation = hex(decimal_num)

    print(f"Decimal: {decimal_num}")
    print(f"Binary: {binary_representation}")
    print(f"Octal: {octal_representation}")
    print(f"Hexadecimal: {hexadecimal_representation}")

# Example usage:
decimal_input = 255
convert_decimal(decimal_input)

decimal_input_2 = 42
convert_decimal(decimal_input_2)