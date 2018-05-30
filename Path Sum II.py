'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.find(root, sum, [], res)
        return res
    
    def find(self, node, sum, tmp, res):
        if node.left:
            if node.right:
                self.find(node.left, sum - node.val, tmp + [node.val], res)
                self.find(node.right, sum - node.val, tmp + [node.val], res)
            else:
                self.find(node.left, sum - node.val, tmp + [node.val], res)
        else:
            if node.right:
                self.find(node.right, sum - node.val, tmp + [node.val], res)
            else:
                if node.val == sum:
                    res.append(tmp + [node.val])
            
