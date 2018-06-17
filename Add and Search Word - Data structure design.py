'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if not word:
            return
        
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
                
            node = node.children[w]
        node.is_word = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        if not word:
            return False
        
        self.res = False
        self.find(self.root, word)
        return self.res 
    
    def find(self, node, word):
        if not word:
            if node.is_word:
                self.res = True
                return
        elif word[0] == '.':
            for c in node.children:
                self.find(node.children[c], word[1:])
        else:
            if word[0] in node.children:
                self.find(node.children[word[0]], word[1:])
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
