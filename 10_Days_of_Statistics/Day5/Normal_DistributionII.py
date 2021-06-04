# Day 5: Normal Distribution II
# X = normal random variable, ie, X ~ N ( miu, stdev )
# miu = mean of normal distribution
# stdev = standard deviation of normal distribution
# x = number of successful outcome
# P(X < x) = 0.5 + 0.5*math.erf((x-miu)/(stdev * 2**0.5))
# Note: P(X < x) = P(X <= x) because P(X = x) = 0 for continuous probability distribution function
# P(a < X < b) = P(X < b) - P(X < a)
# P(X > c) = 1 - P(X < c)

import math

miu, stdev = map(float, input().split())
limit1 = float(input())
limit2 = float(input())

def normal_prob(miu, stdev, x):
    return 0.5 + 0.5*math.erf((x-miu)/(stdev * 2**0.5))

print( '%.2f' %((1 - normal_prob(miu, stdev, limit1)) *100) )
print( '%.2f' %((1 - normal_prob(miu, stdev, limit2)) *100) )
print( '%.2f' %(normal_prob(miu, stdev, limit2) *100) )
# note: need to output percentage (not probability)
