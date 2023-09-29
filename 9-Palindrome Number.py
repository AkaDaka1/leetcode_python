# Given an integer x, return true if x is a 
# palindrome, and false otherwise.
# Follow up: Could you solve it without converting the integer to a string?
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
# Runtime 39ms
# Beats 65.03%of users with Python
# Memory 12.99MB
# Beats 98.84%of users with Python
# ------------------------------------
#
#
# Ver 2
# Using converting the integer to a string
# ------------------------------------
class Solution(object):
    def isPalindrome(self, x):
        if x>=0 and x<10:
            return True
        elif x < 0:
            return False
        else:
            x = str(x)
            a = len(x)
            b = 0
            while a>len(x)//2:
                if x[a-1]==x[b]:
                    b+=1
                    a-=1
                else:
                    return False
            return True
# ------------------------------------
# Runtime 31ms
# Beats 88.85%of users with Python
# Memory 13.14MB
# Beats 75.78%of users with Python
# ------------------------------------
