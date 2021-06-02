"""
Objective
In this challenge, we learn about geometric distributions. Check out the Tutorial tab for learning materials!

Task
The probability that a machine produces a defective product is . What is the probability that the  defect occurs the  item produced?

Input Format

The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of being the first defect for:

1 3
5
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).
"""
#Geometric Distribution I
# X is a geometric random variable
# x is the number of trials required until the first success occurs
# p = probability of success in each trial = 1/3

# probability that a specified number of trials will take place before the first success occurs
# P(X = x) = (1-p)**(x–1) * p   # x = 1st, 2nd, 3rd, etc
# Reference: https://www.dummies.com/education/math/business-statistics/how-to-calculate-geometric-probabilities/

def geometric_prob(p, x):
    g = (1-p)**(x-1) * p
    return(g)

numerator, denominator = map(float, input().split())
x = int(input())
p = numerator/denominator
g = geometric_prob(p, x)  
print("%.3f" %g)
