# Strong Password
# https://www.hackerrank.com/challenges/strong-password/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    c_numbers=c_lower_case=0
    c_upper_case=c_special_characters=0
    
    for i in password:
        if i in numbers:
            c_numbers=1
        elif i in lower_case:
            c_lower_case=1
        elif i in upper_case:
            c_upper_case=1
        elif i in special_characters:
            c_special_characters=1
    count=4-c_numbers-c_lower_case-c_upper_case-c_special_characters
    if len(password)+count>=6:
        return count
    else:
        return max(6-len(password),count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
