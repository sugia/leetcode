'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not self.valid(beginWord, endWord, wordList):
            return []
        
        box = set(wordList)
        dic = {beginWord: [[beginWord]]}
        
        vec = [beginWord]
        while vec:
            word = vec.pop(0)
            if word == endWord:
                return dic[word]
            for i in xrange(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in box:
                        if next_word not in dic:
                            dic[next_word] = []
                        if dic[next_word] and len(dic[next_word][0]) <= len(dic[word][0]):
                            continue
                        modified = False
                        for x in dic[word]:
                            if next_word not in x and x + [next_word] not in dic[next_word]:
                                dic[next_word].append(x + [next_word])
                                modified = True
                        if modified:
                            vec.append(next_word)
            
        return []
        
    def valid(self, beginWord, endWord, wordList):
        box = set(wordList)
        vec = [(beginWord, 1)]
        while vec:
            word, length = vec.pop(0)
            if word == endWord:
                return length
            for i in xrange(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in box:
                        box.remove(next_word)
                        vec.append((next_word, length+1))
        return 0
        
