# On exam/midterm

investment = eval(input("Enter investment amount: "))
annualRate = eval(input("Enter the annual interest rate: "))
years = eval(input("Enter the number of years: "))

monthlyRate = annualRate / 1200
numberMonths = years * 12

futureValue = investment * ((1 + monthlyRate) ** numberMonths)

print("Accumulated value is: ", futureValue)