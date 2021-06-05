# Day 7: Spearman's Rank Correlation Coefficient
def get_rank(X):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]
    
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rx = get_rank(X)
ry = get_rank(Y)

d = [(rx[i] -ry[i])**2 for i in range(n)]
r_s = 1 - (6 * sum(d)) / (n * (n*n - 1))
print('%.3f' % r_s)

