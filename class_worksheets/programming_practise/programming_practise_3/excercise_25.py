bottom = int(input())
top = int(input())

def exponent(bottom, top):
    number = top
    result = 1
    while number > 0:
        result = result * bottom
        number = number - 1
    print(bottom, "to the power off", top, "is", result)

exponent(bottom, top)