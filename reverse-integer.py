class Solution:
    #given an integer
    #return an integer
    def reverse(self, x):
        if x == 0:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x //= 10
        y *= sign
        if y > 2147483647:
            return 0
        if y < -2147483648:
            return 0
        return y
