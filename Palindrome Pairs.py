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
        dic = {}
        for i in xrange(len(words)):
            dic[words[i][::-1]] = i
            
        res = []
        for i in xrange(len(words)):
            for j in xrange(len(words[i])+1):
                prefix = words[i][:j]
                suffix = words[i][j:]
                if prefix in dic and suffix == suffix[::-1] and i != dic[prefix] and [i, dic[prefix]] not in res:
                    res.append([i, dic[prefix]])
                if suffix in dic and prefix == prefix[::-1] and i != dic[suffix] and [dic[suffix], i] not in res:
                    res.append([dic[suffix], i])
        return res
