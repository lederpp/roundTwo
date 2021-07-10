# Look Over **** number of monthes is number of years times 12, not divided by 12!

endValue = eval(input("Enter the desired final account value: "))
annualRate = eval(input("Enter the interest rate percentage: "))
numYear = eval(input("Enter number of years: "))

numMonths = numYear * 12                      # years x 12 **** Look over, keep confusing it
monthlyRate = annualRate / 1200               # 12 * 100


initialDeposit = endValue / (1 + monthlyRate) ** numMonths

print("The inital deposit amount needed is: ", initialDeposit)