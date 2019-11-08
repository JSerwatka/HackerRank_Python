# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB, BC = int(input()), int(input())

AC = math.sqrt(AB**2 + BC**2)
y = AC / 2
z = math.sin(math.acos(AB/AC)) * y
b = math.sqrt(y**2 - z**2)
a = AB - b
gamma = math.atan(z/a)
fi = 90 - math.degrees(gamma)

print(str(round(fi)) + "\N{DEGREE SIGN}")
