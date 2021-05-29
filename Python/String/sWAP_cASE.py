"""# sWAP cASE

# You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

# Input Format
# A single line containing a string S.

# Constraints
# 0 < len(S) <= 1000

# Output Format
# Print the modified string S.

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
def swap_case(s):
    t = []
    for i in range(0,len(s)):
        if s[i] in upper :
            t.append(s[i].lower)
        elif s[i] in lower:
            t.append(s[i].upper)
        else :
            t.append(s[i])
    return ' '.join(t)
if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
