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
                
        counter = 0
        begin = 0
        end = 0
        res = (float('-inf'), float('inf'))
        
        while end < len(s):
            if s[end] in dic:
                if dic[s[end]] > 0:
                    counter += 1
                dic[s[end]] -= 1
            end += 1
            while counter == len(t):
                if res[1] - res[0] > end - begin:
                    res = (begin, end)
                if s[begin] in dic:
                    if dic[s[begin]] == 0:
                        counter -= 1
                    dic[s[begin]] += 1
                begin += 1
                    
        if res == (float('-inf'), float('inf')):
            return ""
        return s[res[0]:res[1]]
                        
