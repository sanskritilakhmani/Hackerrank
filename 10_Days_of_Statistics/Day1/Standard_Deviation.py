"""
Objective
In this challenge, we practice calculating standard deviation. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of  decimal place (i.e.,  format). An error margin of  will be tolerated for the standard deviation.

Example

The sum of the array values is  and there are  elements. The mean is .
Subtract the mean from each element, square each result, and take their sum.






Their sum is 18. Take the square root of  to get , the standard deviation.

Function Description

Complete the stdDev function in the editor below.

stdDev has the following parameters:
- int arr[n]: an array of integers

Prints
- float: the standard deviation to 1 place after the decimal

Input Format

The first line contains an integer, , denoting the size of arr.
The second line contains  space-separated integers that describe .

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(numbers):
    # Print your answers to 1 decimal place within this function
    mean = sum(numbers) / n
    variance = sum([((x - mean) ** 2) for x in numbers]) / n
    stddev = variance ** 0.5
    print("{:.1f}".format(stddev))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
