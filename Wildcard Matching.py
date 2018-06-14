'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx = 0
        p_idx = 0
        
        ss_idx = -1
        pp_idx = -1
        while s_idx < len(s):
            if p_idx < len(p) and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                p_idx += 1
                s_idx += 1
            elif p_idx < len(p) and p[p_idx] == '*':
                pp_idx = p_idx
                p_idx = pp_idx + 1
                ss_idx = s_idx
            elif pp_idx != -1:
                p_idx = pp_idx + 1
                ss_idx += 1
                s_idx = ss_idx
            else:
                return False
        
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len(p)
                
