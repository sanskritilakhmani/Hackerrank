# Day 6: The Central Limit Theorem I
import math

def normal_prob(miu, stdev, x):
    return 0.5 + 0.5*math.erf((x-miu)/(stdev * 2**0.5))

weight_limit = float(input())
n = int(input())
[miu, stdev] = [float(input()) for _ in range(2)]

# By Central Limit Thereom, for large n, 
# S ~ N(miu_S, stdev_S) approximately
miu_S = n*miu
stdev_S = (n**0.5)*stdev

# To find P(S < weight_limit)
print( '%.4f' %normal_prob(miu_S, stdev_S, weight_limit) )
