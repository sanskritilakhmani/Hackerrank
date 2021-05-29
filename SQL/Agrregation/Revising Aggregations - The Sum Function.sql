/*
Query the total population of all cities in CITY where District is California.

Input Format

The CITY table is described as follows: CITY.jpg

*/
Select SUM(POPULATION) From CITY where DISTRICT = 'California';
