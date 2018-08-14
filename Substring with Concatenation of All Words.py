'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []


'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if not s or not words or not words[0]:
            return res
        
        wdic = {}
        for word in words:
            if word in wdic:
                wdic[word] += 1
            else:
                wdic[word] = 1
                
        
        for i in xrange(len(s) - len(words) * len(words[0]) + 1):
            tdic = {}
            for j in xrange(len(words)):
                tmp = s[i + j * len(words[0]): i + (j+1) * len(words[0])]
                if tmp in wdic:
                    if tmp in tdic:
                        tdic[tmp] += 1
                    else:
                        tdic[tmp] = 1
                    if tdic[tmp] > wdic[tmp]:
                        break
                    if tdic == wdic:
                        res.append(i)
                else:
                    break
        return res
                    
