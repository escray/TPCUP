import math

rediusString = raw_input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInterger ** 2)

print "The circumference is: ", circumference, ", and the area is :", area
