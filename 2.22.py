# Look Over

years = eval(input("Enter the number of years: "))

currentPop = 312032486
secYear = 365 * 24 * 60 * 60        # Seconds in year *****

growthPerYear = currentPop + (years * secYear // 7) - (years * secYear // 13) + (years * secYear // 45)


print("The population in ", years, "years is ", growthPerYear)
