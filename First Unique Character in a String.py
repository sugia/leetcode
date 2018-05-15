'''

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_to_idx_vec = {}
        
        for i in xrange(len(s)):
            if s[i] in char_to_idx_vec:
                char_to_idx_vec[s[i]].append(i)
            else:
                char_to_idx_vec[s[i]] = [i]
                
        for i in xrange(len(s)):
            if len(char_to_idx_vec[s[i]]) == 1:
                return i
            
        return -1
