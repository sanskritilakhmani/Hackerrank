/*
You are given  triangles, specifically, their sides ,  and . Print them in the same style but sorted by their areas from the smallest one to the largest one. It is guaranteed that all the areas are different.

The best way to calculate a area of a triangle with sides ,  and  is Heron's formula:

 where .

Input Format

The first line of each test file contains a single integer .  lines follow with three space-separated integers, ,  and .

Constraints

, and 
Output Format

Print exactly  lines. On each line print  space-separated integers, the ,  and  of the corresponding triangle.

Sample Input 0

3
7 24 25
5 12 13
3 4 5
Sample Output 0

3 4 5
5 12 13
7 24 25
Explanation 0

The square of the first triangle is . The square of the second triangle is . The square of the third triangle is . So the sorted order is the reverse one.

*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    int *p=malloc(n*sizeof(float)); 
//create array of size n to store "volumes"
    for(int i=0;i<n;i++)
    {
 float a=(tr[i].a+tr[i].b+tr[i].c)/2.0;
//use 2.0 compulsary int/int gives int, int/float gives float
       p[i]=(a*(a-tr[i].a)*(a-tr[i].b)*(a-tr[i].c));
//formula without sqrt as areas are different guarenteed 
//because sqrt dosent work well with float values
    }
//bubble sort
    for(int i=0;i<n;i++)    
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(p[j]>p[j+1])     
            {
                int temp=p[j];
                p[j]=p[j+1];
                p[j+1]=temp;
//swapping array of areas in ascending
//and simuntaneously the structure contents
                temp=tr[j].a;
                tr[j].a=tr[j+1].a;
                tr[j+1].a=temp;
                temp=tr[j].b;
                tr[j].b=tr[j+1].b;
                tr[j+1].b=temp;
                temp=tr[j].c;
                tr[j].c=tr[j+1].c;
                tr[j+1].c=temp;
            }
        }
    }
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
