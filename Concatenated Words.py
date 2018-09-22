'''
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
'''

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dic = {}
        for a in words:
            for b in words:
                if b != a and b in a:
                    if a not in dic:
                        dic[a] = set([b])
                    else:
                        dic[a].add(b)
        
        res = []
        for a in dic:
            if self.valid(a, dic[a]):
                res.append(a)
        return res
    
    def valid(self, s, words):
        f = {-1: True}
        for i in xrange(len(s)):
            f[i] = False
            for word in words:
                if i - len(word) >= -1 and f[i-len(word)] and s[i-len(word)+1:i+1] == word:
                    f[i] = True
                    break
        return f[len(s)-1]
