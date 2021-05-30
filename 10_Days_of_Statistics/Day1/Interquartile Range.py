"""
Objective
In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

Task
The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).

Given an array, , of  integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each  occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of  decimal place (i.e.,  format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

Example


Apply the frequencies to the values to get the expanded array . Here . The median of the left half, , the middle element. For the right half, . Print the difference to one decimal place: , so print .

Function Description

Complete the interQuartile function in the editor below.

interQuartile has the following parameters:
- int values[n]: an array of integers
- int freqs[n]:  occurs  times in the array to analyze

Prints

float: the interquartile range to 1 place after the decimal
Input Format

The first line contains an integer, , the number of elements in arrays  and .
The second line contains  space-separated integers describing the elements of array .
The third line contains  space-separated integers describing the elements of array .

Constraints

The number of elements in  is equal to .
Output Format

Print the interquartile range for the expanded data set on a new line. Round the answer to a scale of  decimal place (i.e.,  format).

Sample Input

STDIN           Function
-----           --------
6               arrays size n = 6
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
from statistics import median
def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    
    new_list = []
    for i in range(len(values)):
        for j in range(freqs[i]):
            new_list.append(values[i])


    n = len(new_list)
    x = sorted(new_list)    
    Q1 = median(x[:n//2])
    Q3 = median(x[(n+1)//2:])
    print("{:.1f}".format(Q3-Q1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
