class Solution:
    #given a string
    #return an integer
    def longestValidParentheses(self, s):
        inc = []
        left = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                inc.append(i)
            else:
                if len(inc) == 0:
                    left = i + 1
                else:
                    inc.pop()
                    if len(inc) == 0:
                        res = max(res, i - left + 1)
                    else:
                        res = max(res, i - inc[-1])
        return res
