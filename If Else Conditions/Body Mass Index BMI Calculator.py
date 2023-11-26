# BMI Calculator

print("Welcome to the Body Mass Index (BMI) Calculator!")

weight = float(input("Please enter your weight in kilograms (kgs): "))
height = float(input("Now enter your height in meters (m): "))

# To calculate BMI, we only need the above two values. BMI = weight (kgs) / height^2 (m^2)
BMI = weight / height**2

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
        print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
        print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
        print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese")