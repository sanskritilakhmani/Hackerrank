# Day 5: Poisson Distribution II
# Given cost_A = 160 + 40*X**2
# Expectation of cost_A
# E(cost_A) = E(160 + 40*X**2)
# = E(160) + E(40*X**2)
# = 160 + 40*E(X**2)
# By definition, E(X**2) = E(X) + (E(X))**2 and E(X) = miu_A
# Therefore E(cost_A) = 160 + 40*(miu_A + (miu_A)**2)

# Given cost_B = 128 + 40*Y**2
# Expectation of cost_B
# E(cost_B) = E(128 + 40*Y**2)
# = E(128) + E(40*Y**2)
# = 128 + 40*E(Y**2)
# By definition, E(Y**2) = E(Y) + (E(Y))**2 and E(Y) = miu_B
# Therefore E(cost_B) = 128 + 40*(miu_B + (miu_B)**2)

miu_A, miu_B = map(float, input().split())

cost_A = 160 + 40*(miu_A + miu_A**2)
print(round(cost_A, 3))
cost_B = 128 + 40*(miu_B + miu_B**2)
print(round(cost_B, 3))
