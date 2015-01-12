class Solution:
    #given a string
    #return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        res = 0
        left = 0
        right = 0
        can = set()
        while right < len(s):
            while right < len(s) and s[right] not in can:
                can.add(s[right])
                right += 1
            res = max(res, right - left)
            if right >= len(s):
                break
            while s[left] != s[right]:
                can.remove(s[left])
                left += 1
            can.remove(s[left])
            left += 1
        return res
