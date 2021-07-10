# Look Over

num = eval(input("Enter an integer between 0 & 1000: "))

num1 = num % 10
num //= 10
num2 = num % 10
num //= 10
num3 = num

print("The sum of the digits in the integer: ", num1 + num2 + num3)