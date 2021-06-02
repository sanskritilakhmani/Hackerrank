
# Day 4: Binomial Distribution I
"""
Objective
In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

Task
The ratio of boys to girls for babies born in Russia is . If there is  child born per birth, what proportion of Russian families with exactly  children will have at least  boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).

Input Format

A single line containing the following values:

1.09 1
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places 
"""
import math

def binomial_prob(n, p, x):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

boy, girl = map(float, input().split())
n = 6
p = boy/(boy+girl)
b = 0
for x in range(3,7): # x=3,4,5,6
    b += binomial_prob(n, p, x)   
print("%.3f" %b)
