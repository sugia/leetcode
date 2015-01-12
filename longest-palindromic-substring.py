class Solution:
    #given a string
    #return a string
    def longestPalindrome(self, s):
        t = '_'
        for x in s:
            t += x + '_'
        r = [0 for i in range(len(t))]
        mid = 0
        right = 0
        for i in range(1, len(t)-1):
            if i > right:
                r[i] = self.cal(t, i, i)
                mid = i
                right = i + r[i]
            else:
                j = mid - (i - mid)
                width = right - i
                if r[j] == width:
                    r[i] = width + self.cal(t, i-width, i+width)
                    mid = i
                    right = i + r[i]
                else:
                    r[i] = min(r[j], width)
        mid = 1
        for i in range(1, len(t)-1):
            if r[i] > r[mid]:
                mid = i
        res = ''
        for i in range(mid - r[mid], mid + r[mid]):
            if i & 1:
                res += t[i]
        return res
    def cal(self, t, l, r):
        w = 0
        while l-(w+1) >= 0 and r +(w+1) < len(t) and t[l-(w+1)] == t[r+(w+1)]:
            w += 1
        return w
