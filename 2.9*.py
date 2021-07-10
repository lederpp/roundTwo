
tempF = eval(input("Enter the temperature in Fahrenheit between -58 & 41: "))
windS = eval(input("Enter the wind speed in MPH: "))

windV = windS ** 0.16

windChill = 35.74 + (0.6215 * tempF) - (35.75 * windV) + (0.4275 * tempF * windV)

print("The windchill index is: ", windChill)