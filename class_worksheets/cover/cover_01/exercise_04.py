import math
def factorial(n):
    result = math.factorial(n)
    return result
n = int(input("Enter number"))
print("the factorial is", factorial(n))

def gcd(a, b):
    if b != 0 and a != 0:
        return gcd(b, a % b)
a = int(input("Enter number"))
b = int(input("Enter number"))
print("The GCD is" , gcd(a, b))
