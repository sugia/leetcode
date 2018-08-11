'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

    Both of the given trees will have between 1 and 100 nodes.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1:
            return root2 != None
        if not root2:
            return root1 != None
        
        a = []
        self.find(root1, a)
        
        b = []
        self.find(root2, b)
        
        if len(a) != len(b):
            return False
        for i in xrange(len(a)):
            if a[i] != b[i]:
                return False
            
        return True
    
    def find(self, node, res):
        if node.left:
            self.find(node.left, res)
            
        if not node.left and not node.right:
            res.append(node.val)
            
        if node.right:
            self.find(node.right, res)
