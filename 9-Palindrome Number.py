# Given an integer x, return true if x is a 
# palindrome, and false otherwise.
# ------------------------------------
class Solution(object):
    def isPalindrome(self, x):
        arr = []
        if x >= 10:
            while x > 0:
                arr += [x%10]
                x//=10
            leng = len(arr)
            while leng > 0:
                if arr == arr[::-1]:
                    return True
                else:
                    return False
        elif x>=0 and x<10:
            return True
        else:
            return False
# ------------------------------------
# Runtime
# 39ms
# Beats 65.03%of users with Python

# Memory
# 12.99MB
# Beats 98.84%of users with Python
