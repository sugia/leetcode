'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dic = {}
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        counter = len(t)
        
        res = ''
        i = 0
        for j in xrange(len(s)):
            if s[j] in dic:
                dic[s[j]] -= 1
                if dic[s[j]] >= 0:
                    counter -= 1
            
            while counter == 0:
                if res == '' or len(res) > j - i + 1:
                    res = s[i:j+1]
                
                if s[i] in dic:
                    dic[s[i]] += 1
                    if dic[s[i]] > 0:
                        counter += 1
                i += 1
                
        return res
