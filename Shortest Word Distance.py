'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return 0
        
        word_idx = {}
        for i in xrange(len(words)):
            if words[i] not in word_idx:
                word_idx[words[i]] = [i]
            else:
                word_idx[words[i]].append(i)
                
        res = float('inf')
        i = 0
        j = 0
        while i < len(word_idx[word1]) and j < len(word_idx[word2]):
            res = min(res, abs(word_idx[word1][i] - word_idx[word2][j]))
            if word_idx[word1][i] < word_idx[word2][j]:
                i += 1
            else:
                j += 1
                
        return res
