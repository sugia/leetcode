class Solution:
    #given an integer
    #return a string
    def countAndSay(self, n):
        t = '1'
        for i in range(2, n+1):
            t = self.cal(t)
        return t
    def cal(self, s):
        t = ''
        left = 0
        while left < len(s):
            right = left + 1
            while right < len(s) and s[right] == s[left]:
                right += 1
            t += str(right - left) + s[left]
            left = right
        return t
