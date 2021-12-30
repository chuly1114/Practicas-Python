#returning values
def area_triangle(base, height):
    return (base * height / 2)


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
Area = area_a + area_b
print("The sum of both areas is: " + str(Area))
