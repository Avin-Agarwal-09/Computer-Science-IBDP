Side1 = int(input("Enter your side 1: "))
Side2 = int(input("Enter your side 2: "))
Side3 = int(input("Enter your side 3: "))
if Side1<1 or Side2<1 or Side3<1:
    print("invalid triangle")
elif Side1 == Side2  or Side1 == Side3 or Side2 == Side3:
    print("isosceles")
elif Side1 == Side2 == Side3:
    print("Equilateral")
elif not (Side1 == Side2 or Side1 == Side3 or Side2 == Side3):
    print("Scalene")

