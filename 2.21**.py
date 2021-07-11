# Look Over

save = eval(input("Enter the monthly saving amount: "))

M_I_R = 0.00417

total = save * (1 + M_I_R)
total = (save + total) * (1 + M_I_R)
total = (save + total) * (1 + M_I_R)
total = (save + total) * (1 + M_I_R)
total = (save + total) * (1 + M_I_R)
total = (save + total) * (1 + M_I_R)

print("After the sixth month, the account value is: ", total)