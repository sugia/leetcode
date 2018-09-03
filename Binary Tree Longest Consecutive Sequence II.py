'''
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
Note: All the values of tree nodes are in the range of [-1e7, 1e7].
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
            return 0, 0
        left = self.find(node.left)
        right = self.find(node.right)
        inc = 1
        dec = 1
        if node.left and node.val+1 == node.left.val:
            inc = max(inc, 1+left[0])
        if node.right and node.val+1 == node.right.val:
            inc = max(inc, 1+right[0])
        
        if node.left and node.val-1 == node.left.val:
            dec = max(dec, 1+left[1])
        if node.right and node.val-1 == node.right.val:
            dec = max(dec, 1+right[1])
        self.res = max(self.res, inc+dec-1)
        return inc, dec
