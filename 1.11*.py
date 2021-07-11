# Look over   (Look at assignment #1, solved it differently)

currentPop = 312032486
secYear = 365 * 24 * 60 * 60        # Seconds in year *****

growthPerYear = currentPop + secYear / 7 - secYear / 13 + secYear / 45

year1 = growthPerYear
year2 = 2 * growthPerYear
year3 = 3 * growthPerYear
year4 = 4 * growthPerYear
year5 = 5 * growthPerYear

print(year1, year2, year3, year4, year5)


