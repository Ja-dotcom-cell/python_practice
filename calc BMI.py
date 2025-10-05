weight=float(input("Enter your weight: "))
height=float(input("Enter your height(in ft):"))
height_1=height*0.3048
BMI=weight/(height_1**2)
print(f"Your BMI is {BMI}")
if BMI < 16:
    print("You are Underweight (Severe thinness).")
elif BMI >= 16 and BMI <= 17:
    print("You are Underweight (Moderate thinness).")
elif BMI >= 17 and BMI <= 18.5:
    print("You are Underweight (Mild thinness).")
elif BMI >= 18 and BMI < 25:
    print("You are Normal range.")
elif BMI >= 25 and BMI < 30:
    print("You are Overweight (Pre-obese).")
elif BMI >= 30 and BMI < 35:
    print("You are Obese (Class I).")
elif BMI >= 35 and BMI < 40:
    print("You are Obese (Class II).")
elif BMI >=40:
    print("You are Obese (Class III)")
else:
    print("Invalid input.")