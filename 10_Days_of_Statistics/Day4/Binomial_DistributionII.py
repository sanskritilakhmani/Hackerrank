
# Day 4: Binomial Distribution II
"""
Objective
In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
A manufacturer of metal pistons finds that, on average,  of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of  pistons will contain:

No more than  rejects?
At least  rejects?
Input Format

A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):

12 10
"""
import math

def binomial_prob(n, p, x):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

reject_percent, n = map(float, '12 10'.split())
p = reject_percent/100
b = 0
for x in range(0,3): # x=0,1,2
    b += binomial_prob(n, p, x)   
print("%.3f" %b)
print(round(sum([binomial_prob(n, p, i) for i in range(2, 11)]), 3))  # x=2,3,4,...,10
