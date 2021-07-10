# eval() is bad practice. Can lead to security issues and so on

count = 0
for i in range(0, 10, 2):
    i += i
    print(i)