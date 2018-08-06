'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].

'''

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False
        
        dic = {}
        for c in s1:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
                
        for i in xrange(len(s1) - 1):
            if s2[i] in dic:
                dic[s2[i]] -= 1
                
        for i in xrange(len(s1) - 1, len(s2)):
            if s2[i] in dic:
                dic[s2[i]] -= 1
            if self.match(dic):
                return True
            if s2[i + 1 - len(s1)] in dic:
                dic[s2[i + 1 - len(s1)]] += 1
                
        return False
    
    def match(self, dic):
        for k, v in dic.iteritems():
            if v != 0:
                return False
        return True
