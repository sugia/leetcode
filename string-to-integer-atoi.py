class Solution:
    #given a string
    #return an integer
    def atoi(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]
        res = 0
        for x in s:
            if '0' <= x <= '9':
                res = res * 10 + int(x)
            else:
                break
        res *= sign
        res = max(res, -2147483648)
        res = min(res, 2147483647)
        return res
