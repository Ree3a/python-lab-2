#7. Given a positive real number, print its fractional part.

number = float(input("Enter the number:"))
import math

fractional_part = math.modf(number)
print(fractional_part)
