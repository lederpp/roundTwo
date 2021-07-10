# Look Over

year = 365                                          # Days
num = eval(input("Enter the number of minutes: "))

numYear = num // (60 * 24 * 365)
numDay = num % (60 * 24 * 365) // (60 * 24)

print(num, "minutes is approximately ", numYear, "years and ", numDay, "days")