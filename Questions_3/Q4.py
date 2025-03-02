import math

# Create a function that returns boh the area and circumference 
# of a circle given its radius

def circle_stats(radius):
  area =  math.pi * radius ** 2
  circumference = 2 * math.pi * radius

  return area , circumference


area , circumference = circle_stats(4)

print("Area: {:.2f} cirumference: {:.2f}".format(area, circumference))