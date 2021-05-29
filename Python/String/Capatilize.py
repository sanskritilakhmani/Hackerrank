"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.
Input Format
A single line of input containing the full name, S.
Output Format
Print the capitalized string, S.
Constraints
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
Sample Input
chris alan
Sample Output
Chris Alan
Sample Input
1 w 2 r 3g
Sample Output
1 W 2 R 3g
"""
1.
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w'
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
 2.
 !/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
