'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        count = [0] * 26
        
        for c in p:
            count[ord(c) - ord('a')] += 1
            
        left = 0
        right = 0
        res = []
        while right < len(s):
            count[ord(s[right]) - ord('a')] -= 1
            while left <= right and count[ord(s[right]) - ord('a')] < 0:
                count[ord(s[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(p):
                res.append(left)
                
            right += 1
            
        return res
            
