"""Topic 2 - Data types and number systems.

Converting between binary (base 2), decimal (base 10) and hexadecimal (base 16)
by hand, rather than with bin() / hex() / int(s, base).

Two techniques cover every conversion:
  to decimal   - positional weighting (multiply each digit by base ** position)
  from decimal - repeated division, reading the remainders bottom-up
"""

HEX_DIGITS = "0123456789ABCDEF"


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


def hex_to_decimal(hex_str):
    value = 0
    exponent = len(hex_str) - 1
    for digit in hex_str.upper():
        value += HEX_DIGITS.index(digit) * (16 ** exponent)
        exponent -= 1
    return value


def decimal_to_hex(n):
    if n == 0:
        return "0"
    hex_str = ""
    while n > 0:
        hex_str = HEX_DIGITS[n % 16] + hex_str
        n = n // 16
    return hex_str


def binary_to_hex(binary_str):
    """Each hex digit is exactly 4 binary digits, so pad then group in fours."""
    padding = (4 - len(binary_str) % 4) % 4
    binary_str = "0" * padding + binary_str

    hex_str = ""
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i + 4]
        hex_str += HEX_DIGITS[binary_to_decimal(nibble)]
    return hex_str


def hex_to_binary(hex_str):
    binary = ""
    for digit in hex_str.upper():
        nibble = decimal_to_binary(HEX_DIGITS.index(digit))
        binary += nibble.rjust(4, "0")
    return binary.lstrip("0") or "0"


if __name__ == "__main__":
    print("1011 binary  ->", binary_to_decimal("1011"), "decimal")
    print("11 decimal   ->", decimal_to_binary(11), "binary")
    print("2F hex       ->", hex_to_decimal("2F"), "decimal")
    print("47 decimal   ->", decimal_to_hex(47), "hex")
    print("101111 binary->", binary_to_hex("101111"), "hex")
    print("2F hex       ->", hex_to_binary("2F"), "binary")
