# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(s):
    n = len(s)
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
    res = 0
    for i in range(n):
        if i > 0 and roman[s[i]] > roman[s[i-1]]:
            res += roman[s[i]] - 2*roman[s[i-1]]
        else:
            res += roman[s[i]]
    retrun res