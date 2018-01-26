# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(x):
    if x == 0 or x > (2**(31)-1) or x < -(2**(31)):
        return x
    else:
        sign = x > 0
        if not sign:
            x = -x
        res = 0
        while x>0:
            res = res * 10 + x%10
            x = int(x/10)
        if res > (2**(31)-1) or res < -(2**(31)):
            return 0
        if sign:
            return res
        else:
            return -res

x = 1534236469
print(reverse(x))