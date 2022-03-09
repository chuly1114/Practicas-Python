"""This is the main module of easiest.py"""
import sys


def main():
    """Any given three sides wont necessarily form
    a triangle.Triangles are categorized depending on the values of the
    sides of a valid triangle.This problem you are required to determine the type of a triangle"""
    triangle = []
    test_cases = int(input(""))
    for i in range(test_cases):
        sides = input("")
        sides = sides.split(" ")
        for (index, value) in enumerate(sides):
            sides[index] = int(value)
        boolean_left = sides[0] > (sides[1] + sides[2])
        boolean_right = sides[1] > (sides[0] + sides[2])
        boolean_bot = sides[2] > (sides[0] + sides[1])
        boolean = boolean_left or boolean_right or boolean_bot
        equilateral = sides[0] == sides[1] and sides[0] == sides[2]
        scalene = sides[0] != sides[1] and sides[0] != sides[2]
        if boolean:
            triangle += ["Invalid"]
        elif equilateral:
            triangle += ["Equilateral"]
        elif scalene:
            triangle += ["Scalene"]
        else:
            triangle += ["Isosceles"]
    for i in range(test_cases):
        sys.stdout.write("Case " + str(i + 1) + ": " + triangle[i] + "\n")


main()
