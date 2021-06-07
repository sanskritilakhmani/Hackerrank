"""
Objective
In this challenge, we practice using multiple linear regression. Check out the Tutorial tab for learning materials!

Task
Andrea has a simple equation:

for  real constants (, , , , ). We can say that the value of  depends on  features. Andrea studies this equation for  different feature sets  and records each respective value of . If she has  new feature sets, can you help Andrea find the value of  for each of the sets?
Note: You are not expected to account for bias and variance trade-offs.

Input Format

The first line contains  space-separated integers,  (the number of observed features) and  (the number of feature sets Andrea studied), respectively.
Each of the  subsequent lines contain  space-separated decimals; the first  elements are features , and the last element is the value of  for the line's feature set.
The next line contains a single integer, , denoting the number of feature sets Andrea wants to query for.
Each of the  subsequent lines contains  space-separated decimals describing the feature sets.

Constraints

Scoring
For each feature set in one test case, we will compute the following:

. We will permit up to a  margin of error.
The normalized score for each test case will be: . If the challenge is worth  points, then your score will be .

Output Format

For each of the  feature sets, print the value of  on a new line (i.e., you must print a total of  lines).

Sample Input

2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18
Sample Output

105.22
142.68
132.94
129.71
Explanation

We're given , so . We're also given , so we determine that Andrea studied the following feature sets:

We use the information above to find the values of , , and . Then, we find the value of  for each of the  feature sets.
"""
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
