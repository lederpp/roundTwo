# Look Over

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle(seperated by commas): "))

s1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5     #  ** 0.5 is square-root
s2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
s3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5

s = (s1 + s2 + s3) / 2
area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5

print("The area of the traingle is: ", area)