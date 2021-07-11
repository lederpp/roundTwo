
weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))

kG = 0.45359237 * weight                  # pounds to kg
meters = 0.0254 * height                    # inches to meters

bmi = kG / (meters ** 2)

print("BMI is: ", bmi)
