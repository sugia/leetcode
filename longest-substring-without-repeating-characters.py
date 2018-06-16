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

    
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        begin = 0
        end = 0
        while end < len(s):
            if s[end] in dic:
                dic[s[end]] += 1
            else:
                dic[s[end]] = 1
                
            end += 1
            
            while dic[s[end-1]] > 1:
                if s[begin] in dic:
                    dic[s[begin]] -= 1
                begin += 1
                
            if end - begin > res:
                res = end - begin
                
        return res
