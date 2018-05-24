'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''


class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                return False
            cur = cur.leaves[c]
        return cur.is_string

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if c not in cur.leaves:
                return False
            cur = cur.leaves[c]
        return cur != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
