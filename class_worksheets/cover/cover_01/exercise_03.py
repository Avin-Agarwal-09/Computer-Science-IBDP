weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
BMI = weight / (height * height)
print("Your BMI is:", BMI)
if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI <= 25:
    print("You are normal")
elif BMI >= 25 and BMI <= 30:
    print("You are overweight")
elif BMI >= 30:
    print("You are obese")
