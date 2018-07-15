'''
 Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1

Note:

    words has length in range [1, 15000].
    For each test case, up to words.length queries WordFilter.f may be made.
    words[i] has length in range [1, 10].
    prefix, suffix have lengths in range [0, 10].
    words[i] and prefix, suffix queries consist of lowercase letters only.

'''

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.p = {}
        for word in words:
            for i in xrange(len(word) + 1):
                if word[:i] in self.p:
                    self.p[word[:i]].add(word)
                else:
                    self.p[word[:i]] = set([word])
                    
        self.s = {}
        for word in words:
            for i in xrange(len(word) + 1):
                if word[i:] in self.s:
                    self.s[word[i:]].add(word)
                else:
                    self.s[word[i:]] = set([word])
                    
        self.w = {}
        for i in xrange(len(words)):
            self.w[words[i]] = i

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        
        if prefix not in self.p or suffix not in self.s:
            return -1
        
        box = self.p[prefix] & self.s[suffix]
        
        res = 0
        for x in box:
            res = max(res, self.w[x])
        
        return res


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
