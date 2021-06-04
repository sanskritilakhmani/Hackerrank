# Day 5: Poisson Distribution I
# X = poisson random variable
# x = number of successes that occur in a specified region
# mean = mean number of successes that occur in a specified region
# exp = constant = approximately 2.71828
# P(X = x) = ((mean ** k) * exp(-mean)) / factorial(k)
# Reference: https://stattrek.com/probability-distributions/poisson.aspx

from math import factorial, exp

miu = float(input())
x = int(input())
poisson = ((miu ** x) * exp(-miu)) / factorial(x)
print("%.3f" % poisson)
