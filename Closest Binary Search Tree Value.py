'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = [root.val]
        self.find(root, target, res)
        
        return res[0]
    
    def find(self, node, target, res):
        if abs(res[0] - target) > abs(node.val - target):
            res[0] = node.val
        
        if node.left:
            self.find(node.left, target, res)
            
        if node.right:
            self.find(node.right, target, res)
