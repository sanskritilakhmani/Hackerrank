!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    # Write your code here
    total = k
    fulf =[]
    for i in order:
        if i<= total:
            fulf.append(i)
            total -=i
        else:
            break
    if sum(fulf) > k:
        fulf.pop()
    return len(fulf)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    order_count = int(raw_input().strip())

    order = []

    for _ in xrange(order_count):
        order_item = int(raw_input().strip())
        order.append(order_item)

    k = int(raw_input().strip())

    result = filledOrders(order, k)

    fptr.write(str(result) + '\n')

    fptr.close()
