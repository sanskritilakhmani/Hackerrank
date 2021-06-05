# Day 7: Pearson Correlation Coefficient I
n = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

miu_x = sum(X) / n
miu_y = sum(Y) / n

stdev_x = (sum([(i - miu_x)**2 for i in X]) / n)**0.5
stdev_y = (sum([(i - miu_y)**2 for i in Y]) / n)**0.5

covariance = sum([(X[i] - miu_x) * (Y[i] -miu_y) for i in range(n)])
correlation_coefficient = covariance / (n * stdev_x * stdev_y)
print(round(correlation_coefficient,3))

