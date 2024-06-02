# Roman numerals are represented by seven different symbols: I, V, X, L, C, D, M
# Translate Roman to Integer
# -------------------------------------------

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = list(s)
        x = 0
        res = 0
        while x < len(roman):
            match roman[x]:
                case 'I':
                    roman[x] = 1
                case 'V':
                    roman[x] = 5
                case 'X':
                    roman[x] = 10
                case 'L':
                    roman[x] = 50
                case 'C':
                    roman[x] = 100
                case 'D':
                    roman[x] = 500
                case 'M':
                    roman[x] = 1000
            if x>0:
                if roman[x-1]>=roman[x]:
                    res += roman[x-1]
                else:
                    res -= roman[x-1]
            x += 1
        res += roman[x-1]
        return res

# -------------------------------------------
# Runtime 43 ms
# Beats 74.80%

# Memory 16.54 MB
# Beats 63.94%
