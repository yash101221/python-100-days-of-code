print("BMI Calculator")

height = float(input("Enter your Height(in meters) : \n"))
weight = float(input("Enter your Weight(in kilograms)\n"))

newheight = height*height #For BMI formula

BMI = weight/newheight

if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f} and You are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI:.2f} and You are in normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI:.2f} and You are slightly overweight.")
else:
    print(f"Your BMI is {BMI:.2f} and You are obese.")
