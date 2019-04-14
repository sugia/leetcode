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
class WordDistance:

    def __init__(self, words: List[str]):
        self.dic = {}
        for i, word in enumerate(words):
            if word not in self.dic:
                self.dic[word] = []
            self.dic[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        a = self.dic[word1]
        b = self.dic[word2]
        i = 0
        j = 0
        res = float('inf')
        while i < len(a) and j < len(b):
            res = min(res, abs(a[i] - b[j]))
            if a[i] == b[j]:
                break
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
