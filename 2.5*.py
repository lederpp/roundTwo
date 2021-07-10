subtotal, gratuityRate = eval(input("Enter the subtotal & gratuity rate:"))

tip = (gratuityRate / 100) * subtotal
total = tip + subtotal

print("The gratuity cost is: ", tip, "and the total comes to: ", total)