# Day 4: Geometric Distribution II
# probability that defect is found during the first 5 inspections, 
# ie, 1st batch defect, 2nd batch defect,.., 5th batch defect
"""
Objective
In this challenge, we go further with geometric distributions. We recommend reviewing the Geometric Distribution tutorial before attempting this challenge.

Task
The probability that a machine produces a defective product is . What is the probability that the  defect is found during the first  inspections?

Input Format

The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of the first defect being discovered by:

1 3
5
If you do not wish to read this information from stdin, you can hard-code it into your program.
"""
def geometric_prob(p, x):
    g = (1-p)**(x-1) * p
    return(g)

numerator, denominator = map(float, input().split())
x = int(input())
p = numerator/denominator
g = 0
for i in range(1,6): # i=1,2,3,4,5
    g += geometric_prob(p, i)   
print("%.3f" %g)
