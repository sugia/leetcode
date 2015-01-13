class Solution:
    #given two integers
    #return an integer
    def divide(self, dividend, divisor):
        assert divisor != 0
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        res = 0
        while dividend >= divisor:
            d = divisor
            t = 1
            while d + d <= dividend:
                d += d
                t += t
            dividend -= d
            res += t
        return res * sign
