# Look Over

water = eval(input("Enter the amount of water in kilograms: "))
iTemp = eval(input("Enter the initial temperature: "))
fTemp = eval(input("Enter the final temperature: "))

energy = water * (fTemp - iTemp) * 4184

print("The energy needed is: ", energy)