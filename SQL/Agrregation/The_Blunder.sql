/*
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard’s 0 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeroes removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: actual - miscalculated average monthly salaries), and round it up to the next integer.

Input Format
The EMPLOYEES table is described as follows:

Column	Type
ID	Integer
NAME	String
Salary	Integer
Note: Salary is measured in dollars per month and its value is < 105.

Sample Input

ID	Name	Salary
1	Kristeen	1420
2	Ashley	2006
3	Julia	2210
4	Maria	3000
Sample Output

2061

Explanation
The table below shows the salaries without zeroes as they were entered by Samantha:

ID	Name	Salary
1	Kristeen	142
2	Ashley	26
3	Julia	221
4	Maria	3
Samantha computes an average salary of 98.00. The actual average salary is 2159.00.
The resulting error between the two calculations is 2159.00 - 98.00 = 2061.00 which, when rounded to the next integer, is 2061.

Analysis
We can use REPLACE() function to solve the problem. The syntax is ‘REPLACE(str, from_str, to_str)’ and it returns the string str with all occurrences of the string from_str replaced by the string to_str.

actual average monthly salaries ==> AVG(Salary)
salary without zeros ==> REPLACE(Salary, ‘0’, ‘’)
miscalculated average monthly salaries ==> AVG(REPLACE(Salary, ‘0’, ‘’))
difference between actual and miscalculated average salaries ==>
SELECT AVG(Salary) - AVG(REPLACE(Salary, ‘0’, ‘’))
round the difference up to next integer ==>
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, ‘0’, ‘’)))
from EMPLOYEES table ==> FROM EMPLOYEES
*/
The CEIL() function returns the smallest integer value that is bigger than or equal to a number. Note: This function is equal to the CEILING() function


/*
Enter your query here.
*/
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', ''))) FROM EMPLOYEES;
