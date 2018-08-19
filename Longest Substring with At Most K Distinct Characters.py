'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.


'''

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        box = {}
        res = 0
        start = 0
        for i in xrange(len(s)):
            if s[i] in box:
                box[s[i]] += 1
            else:
                box[s[i]] = 1
            if len(box) <= k:
                res = max(res, i - start + 1)
            while len(box) > k:
                if s[start] in box:
                    box[s[start]] -= 1
                    if box[s[start]] == 0:
                        del box[s[start]]
                start += 1
        return res
                    
