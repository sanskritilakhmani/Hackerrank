"""
Objective
Today we will learn about running time, also known as time complexity. Check out the Tutorial tab for learning materials and an instructional video.

Task
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it is  or .

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code.

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines contains an integer, , to be tested for primality.

Constraints

Output Format

For each test case, print whether  is  or  on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: .
 is divisible by numbers other than  and itself (i.e.: , , , ), so we print  on a new line.

Test Case 1: .
 is only divisible  and itself, so we print  on a new line.

Test Case 2: .
 is only divisible  and itself, so we print  on a new line.
 """
# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_prime(n):
    if n==2:
        return 'Prime'
    elif n==1 or n%2==0:   # 1 or any even number
        return 'Not prime'
    # iterate through for all odd numbers from 3 to int(square root of n)
    for i in range(3, int(n**0.5) + 1, 2):    # 2 step increment, even numbers are not prime
        if n%i==0:
            return 'Not prime'
    return 'Prime'

T = int(input())
for _ in range(T):
    n = int(input())
    print(is_prime(n))
