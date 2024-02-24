import math

length = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))

print("Expected ared:", length*height)

#

n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

Area = (a**2 * n) / (4*math.tan(math.pi/n))
print(Area)

#

height = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print("Expected Output:", (a+b)/2 * height)

#

deg = int(input("Input degree: "))

print("Output radian:", math.radians(deg))