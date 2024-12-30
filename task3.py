# Method 1: Positional Argument
def area_circle_positional(radius):
    from math import pi
    return pi * radius ** 2

radius = float(input("Enter the radius (positional): "))
print("Area (Positional):", area_circle_positional(radius))






# Method 2: First Argument Positional, Second Argument Default
def area_circle_positional_default(radius, pi=3.14159):
    return pi * radius ** 2

radius = float(input("Enter the radius (positional + default): "))
print("Area (Positional + Default):", area_circle_positional_default(radius))






# Method 3: Using Keyword Argument
def area_circle_keyword(*, radius):
    from math import pi
    return pi * radius ** 2

radius = float(input("Enter the radius (keyword): "))
print("Area (Keyword):", area_circle_keyword(radius=radius))






# Method 4: First Argument Keyword, Second Argument Default
def area_circle_keyword_default(*, radius, pi=3.14159):
    return pi * radius ** 2

radius = float(input("Enter the radius (keyword + default): "))
print("Area (Keyword + Default):", area_circle_keyword_default(radius=radius))

