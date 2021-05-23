# Task 
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the
# percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

# Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

# Input Format

# There are 3 lines of numeric input: 
# The first line has a double, mealCost (the cost of the meal before tax and tip). 
# The second line has an integer, tipPercent (the percentage of mealCost being added as tip). 
# The third line has an integer, taxPercent (the percentage of mealCost being added as tax).

# Output Format

# Print The total meal cost is totalCost dollars., where totalCost is the rounded integer result of the entire bill (mealCost with
# added tax and tip).

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = (meal_cost*tip_percent)/100   
    tax = (meal_cost*tax_percent)/100
    total_cost = meal_cost + tip + tax
    return print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

