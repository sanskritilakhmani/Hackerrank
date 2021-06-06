"""
Objective
In this challenge, we practice using linear regression techniques. Check out the Tutorial tab for learning materials!

Task
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, , and Statistics course grade, , can be expressed as the following list of  points:

If a student scored an  on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method, then compute and print the value of  when .

Input Format

There are five lines of input; each line contains two space-separated integers describing a student's respective  and  grades:

95 85
85 95
80 70
70 65
60 70
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).
"""
# Day 8: Least Square Regression Line
# Example 1: using maths formula
# x = [95,85,80,70,60]
# y = [85,95,70,65,70]
x, y = [], []
for _ in range(5):
    i = input().split()
    x.append(int(i[0]))
    y.append(int(i[1]))
n = len(x)
x_sum = sum(x)
x_sum_sqr = x_sum**2
x_sqr_sum = sum([x_i**2 for x_i in x])
y_sum = sum(y)
sum_prod_xy = 0
for x_i,y_i in zip(x,y):
    sum_prod_xy += (x_i*y_i)
b = (n*sum_prod_xy - x_sum*y_sum) / (n*x_sqr_sum - x_sum_sqr)
y_mean = y_sum/n
x_mean = x_sum/n
a = y_mean - b*x_mean

# to make prediction
x_test = 80
y_test = a + b * x_test
print("%.3f" %y_test)   # 78.288

# # Example 2: using Pearson correlation coefficient
# from statistics import mean, pstdev
# def pearson(x, y):
#     n = len(x)
#     mx, sx, my, sy = mean(x), pstdev(x), mean(y), pstdev(y)
#     return sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (n * sx * sy)
# def linear_regression(x, y):
#     b = pearson(x, y) * pstdev(y) / pstdev(x)
#     return mean(y) - b * mean(x), b
# # x = [95,85,80,70,60]
# # y = [85,95,70,65,70]
# x, y = [], []
# for _ in range(5):
#     i = input().split()
#     x.append(int(i[0]))
#     y.append(int(i[1]))
# a, b = linear_regression(x, y)

# # to make prediction
# x_test = 80
# y_test = a + b * x_test
# print("%.3f" %y_test)   # 78.288

