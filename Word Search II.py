'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        dic = {}
        return self.find(pattern, str, dic)
    
    def find(self, pattern, str, dic):
        if not pattern:
            return not str
        
        for i in xrange(1, len(str)+1):
            if pattern[0] in dic and dic[pattern[0]] == str[:i]:
                if self.find(pattern[1:], str[i:], dic):
                    return True
            if pattern[0] not in dic and str[:i] not in dic.values():
                dic[pattern[0]] = str[:i]
                if self.find(pattern[1:], str[i:], dic):
                    return True
                del dic[pattern[0]]
        return False
            
        
