#6510742460 Putthipong
import math
from re import A
def area_of_circular_sector(r, d):
    A = 22/7*pow(r, 2)*d/360
    return A
area_1 = area_of_circular_sector(10, 90)
area_2 = area_of_circular_sector(10, 180)
print(f"Area 1 = {area_1:.2f}, Area 2 = {area_2:.3f}")