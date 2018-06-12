'''
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.


'''

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_value = {}
        left = 0
        res = 0
        for i in xrange(len(s)):
            if len(char_value) == 2 and s[i] not in char_value:
                lowest_value_c = ''
                for c in char_value:
                    if not lowest_value_c or char_value[c] < char_value[lowest_value_c]:
                        lowest_value_c = c
                    
                left = char_value[lowest_value_c] + 1
                del char_value[lowest_value_c]
                
            char_value[s[i]] = i
            res = max(res, i - left + 1)
            
        return res
                
