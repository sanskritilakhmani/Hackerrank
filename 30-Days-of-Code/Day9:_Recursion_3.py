# Day 9: Recursion

# Task 
# Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

# Input Format
# A single integer, N (the argument to pass to factorial).

# Constraints
# 2 <= N <= 12
# Your submission must contain a recursive function named factorial.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n < 1:
        return None
    if n == 1:
        return 1
    return n*factorial(n-1)
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Output Format
# Print a single integer denoting N!.

# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n < 1:
        return None
    if n == 1:
        return 1
    return n*factorial(n-1)
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
