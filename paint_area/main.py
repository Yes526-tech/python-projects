import math
from math import ceil


height = float(input("height:"))
width = float(input("width:"))
coverage = float(input("coverage:"))
which_color = input("which color:")
number_of_cans = height * width / coverage
print(f"you need {ceil(number_of_cans)} cans of {which_color} color.")

#or

def paint_calc(height, width, coverage):
    number_of_cans = height * width / coverage
    color = input("color of wall: ")
    print(f"you need {math.ceil(number_of_cans)} cans of {color} color.")
height_wall = float(input("height:"))
width_wall = float(input("width:"))
coverage_wall = float(input("coverage:"))
paint_calc(height= height_wall, width= width_wall, coverage= coverage_wall)