# Day 9: Multiple Linear Regression
import numpy as np
# import data
[m,n] = list(map(int, input().split()))
x,y = [],[]
for _ in range(n):
    data = input().strip().split(' ')
    x.append(data[0:m])
    y.append(data[-1])
X = np.array(x, float)
y = np.array(y, float)
q = int(input().strip())
X_query = []
for _ in range(q):
    X_query.append(input().strip().split(' '))
X_query = np.array(X_query, float)

#center
X_R = X - np.mean(X, axis=0)
y_R = y - np.mean(y)

#calculate beta
beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)), np.dot(X_R.T,y_R))

#predict
X_query_R = X_query - np.mean(X, axis=0)
y_query_R = np.dot(X_query_R, beta)
y_query = y_query_R + np.mean(y)

#print
for i in y_query:
    print(round(float(i), 2))




## end ##
