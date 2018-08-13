'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]


'''

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_idx = {}
        for idx, word in enumerate(words):
            word_idx[word] = idx
            
        res = []
        for word, idx in word_idx.iteritems():
            for i in xrange(len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]
                
                if self.valid(prefix):
                    tmp = suffix[::-1]
                    if tmp in word_idx and word_idx[tmp] != idx and [word_idx[tmp], idx] not in res:
                        res.append([word_idx[tmp], idx])
                if self.valid(suffix):
                    tmp = prefix[::-1]
                    if tmp in word_idx and word_idx[tmp] != idx and [idx, word_idx[tmp]] not in res:
                        res.append([idx, word_idx[tmp]])
                        
        return res
    
    def valid(self, x):
        return x == x[::-1]
