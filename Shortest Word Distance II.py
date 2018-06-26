'''
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

'''

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        
        self.word_to_idx = {}
        for i in xrange(len(words)):
            if words[i] in self.word_to_idx:
                self.word_to_idx[words[i]].append(i)
            else:
                self.word_to_idx[words[i]] = [i]
        
        self.memory = {}
        
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        if (word1, word2) in self.memory:
            return self.memory[(word1, word2)]
        if (word2, word1) in self.memory:
            return self.memory[(word2, word1)]
        
        if word1 not in self.word_to_idx or word2 not in self.word_to_idx:
            return -1
        
        if word1 == word2:
            return 0
        
        i = 0
        j = 0
        res = float('inf')
        while i < len(self.word_to_idx[word1]) and j < len(self.word_to_idx[word2]):
            if self.word_to_idx[word1][i] < self.word_to_idx[word2][j]:
                res = min(res, self.word_to_idx[word2][j] - self.word_to_idx[word1][i])
                i += 1
            elif self.word_to_idx[word1][i] == self.word_to_idx[word2][j]:
                res = min(res, 0)
                break
            else:
                res = min(res, self.word_to_idx[word1][i] - self.word_to_idx[word2][j])
                j += 1
                
        self.memory[(word1, word2)] = res
        
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
