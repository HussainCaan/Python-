import math
def areaAndCircumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

r = 5
area, circumference = areaAndCircumference(r)
print(f"For a circle with radius {r}:")
print(f"Area: {area}")
print(f"Circumference: {circumference}")