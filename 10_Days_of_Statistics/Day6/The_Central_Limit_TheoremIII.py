# Day 6: The Central Limit Theorem III
# Normal distribution describes that
# 68% population will fall between range +-1 stdev from mean
# 95% population will fall between range +-2 stdev from mean
# 99.7% population will fall between range +-3 stdev from mean
# Reference: https://en.wikipedia.org/wiki/68–95–99.7_rule
# Prob( m-z*s < X < m+z*s ) = 0.95
# z = 1.96

n = int(input())
[miu, stdev] = [float(input()) for _ in range(2)]  # 500, 80
[prob, z] = [float(input()) for _ in range(2)]  # 0.95, 1.96
# population mean ~ N(miu, stdev)
# sample mean ~ N(miu, s), where s = sample stdev = stdev/n**0.5
s = stdev/n**0.5
# lower limit
print('%.2f' %(miu - z*s))
# upper limit
print('%.2f' %(miu + z*s))
