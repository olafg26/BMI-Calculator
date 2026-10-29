#VARIABLES
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kilograms: "))

#PROCESS
BMI = ((weight) / (height ** 2))

#CONDITIONAL BLOCK
if BMI < 18.5:
    print(f"Your BMI is {BMI:.1f}, which is underweight.")
elif BMI <= 24.9:
    print(f"Your BMI is {BMI:.1f}, which is normal weight.")
elif BMI >= 25:
    print(f"Your BMI is {BMI:.1f}, which is overweight.")

