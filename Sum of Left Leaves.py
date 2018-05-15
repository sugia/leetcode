'''

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = []
        self.getLeftLeaves(root, False, res)
        
        return sum(res)
    
    def getLeftLeaves(self, root, isLeftChild, res):
        if not root:
            return
        
        if isLeftChild and not root.left and not root.right:
            res.append(root.val)
            
        self.getLeftLeaves(root.left, True, res)
        
        self.getLeftLeaves(root.right, False, res)
