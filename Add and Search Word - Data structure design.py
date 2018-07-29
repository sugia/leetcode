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
        self.is_end = False

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
        node = self.root
        for c in word:
            if c not in node.children:
                tmp = TrieNode()
                node.children[c] = tmp
            node = node.children[c]
        node.is_end = True
        

    def find(self, root, word):
        node = root
        for i in xrange(len(word)):
            if word[i] == '.':
                flag = False
                for x in node.children:
                    if self.find(node.children[x], word[i+1:]):
                        flag = True
                        break
                if flag:
                    return True
                else:
                    return False
            else:
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
        
        return node != None and node.is_end
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        return self.find(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
