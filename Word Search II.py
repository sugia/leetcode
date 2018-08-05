'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        res = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] in root.children:
                    visited = [[False for jj in xrange(len(board[i]))] for ii in xrange(len(board))]
                    visited[i][j] = True
                    self.find(board, visited, i, j, root.children[board[i][j]], res)
                
        return list(res)
    
    def find(self, board, visited, x, y, node, res):
        if node.word:
            res.add(node.word)
            
        for (i, j) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + i < len(board) and 0 <= y + j < len(board[x+i]):
                if not visited[x+i][y+j] and board[x+i][y+j] in node.children:
                    visited[x+i][y+j] = True
                    self.find(board, visited, x+i, y+j, node.children[board[x+i][y+j]], res)
                    visited[x+i][y+j] = False
        
        
