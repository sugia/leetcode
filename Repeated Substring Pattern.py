'''

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for length in xrange(1, len(s)):
            if len(s) % length != 0:
                continue
            box = set()
            for start in xrange(0, len(s) - length + 1, length):
                # print start, start+length, s[start:start+length]
                token = s[start:start+length]
                box.add(token)
            if len(box) == 1:
                return True
            
        return False
                    
