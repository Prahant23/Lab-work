#Given a positive real number, peint its fractional part,import math
import math

a = float(input("enter the number:" ))
x,y = math.modf(a)
print(x)
print(y)