class Solution:
    #given two strings
    #return an integer
    def strStr(self, s, p):
        if len(p) == 0:
            return 0
        nex = [0]
        cur = 0
        for i in range(1, len(p)):
            while cur > 0 and p[cur] != p[i]:
                cur = nex[cur-1]
            if p[cur] == p[i]:
                cur += 1
            nex.append(cur)
        cur = 0
        for i in range(len(s)):
            while cur > 0 and p[cur] != s[i]:
                cur = nex[cur-1]
            if p[cur] == s[i]:
                cur += 1
            if cur == len(p):
                return i - cur + 1
        return -1
