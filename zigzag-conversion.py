class Solution:
    # @return a string
    def convert(self, s, n):
        if n <= 0:
            return ''
        if n == 1 or n >= len(s):
            return s
        step = n * 2 - 2
        a = step
        b = step
        res = ''
        for i in range(n):
            res += s[i]
            j = i
            while j + a < len(s):
                j += a
                res += s[j]
                if j + b < len(s):
                    j += b
                    res += s[j]
                else:
                    break
            a -= 2
            if a == 0:
                a = step
            if b == step:
                b = 0
            b += 2
        return res
