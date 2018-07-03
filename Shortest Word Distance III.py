'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1

Input: word1 = "makes", word2 = "makes"
Output: 3

Note:
You may assume word1 and word2 are both in the list.

'''

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        a = []
        b = []
        for i in xrange(len(words)):
            if words[i] == word1:
                a.append(i)
            elif words[i] == word2:
                b.append(i)
                
        if a and not b:
            res = float('inf')
            for i in xrange(len(a) - 1):
                if a[i+1] - a[i] < res:
                    res = a[i+1] - a[i]
                
            return res
            

        i = 0
        j = 0
        res = float('inf')
        while i < len(a) and j < len(b):
            if abs(a[i] - b[j]) < res:
                res = abs(a[i] - b[j])
            
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                break
                
        
        return res
