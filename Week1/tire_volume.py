import math

width = int(input("enter the tire of width "  ))
aspect = int(input("enter aspect of the wheel "  ))
diameter = int(input("enter diameter "  ))
volume = math.pi * width**2 * aspect * (width * aspect + 2540 * diameter) / 10_000_000_000
print(f"the approximate volume is {volume:.2f} liters")