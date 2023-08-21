print("Welcome to the BMI calculator!")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = round((weight / height**2),1)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI < 24.9:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 29.9:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 34.9:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")