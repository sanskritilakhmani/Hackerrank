'''
Task
You are given a string  and width . 
Your task is to wrap the string into a paragraph of width .
Input Format
The first line contains a string, . 
The second line contains the width, .
Output Format
Print the text wrapped paragraph.
Sample Input
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output
 ABCD
 EFGH
 IJKL
 IMNO
 QRST
 UVWX
 YZ 
 '''
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
