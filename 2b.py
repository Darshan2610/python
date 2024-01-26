def bintodeci(binary):
    return int(binary, 2)


def octTOhex(octal):
    decimal_value = int(octal, 8)
    return hex(decimal_value)


binary_input = input("Enter a binary number: ")
decimal_result = bintodeci(binary_input)
print(f"Decimal equivalent: {decimal_result}")

octal_input = input("Enter an octal number: ")
hexadecimal_result = octTOhex(octal_input)
print(f"Hexadecimal equivalent: {hexadecimal_result}")
