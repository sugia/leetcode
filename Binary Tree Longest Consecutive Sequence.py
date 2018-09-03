'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.find(root)
        return self.res
    
    def find(self, node):
        if not node:
            return 0
        left = self.find(node.left)
        right = self.find(node.right)
        res = 1
        if node.left and node.val+1 == node.left.val:
            res = max(res, left+1)
        if node.right and node.val+1 == node.right.val:
            res = max(res, right+1)
        self.res = max(self.res, res)
        return res
            
            
