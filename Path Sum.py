'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.find(root, sum)
    
    def find(self, root, sum):
        if not root:
            if sum == 0:
                return True
            else:
                return False
        else:
            if root.left:
                if root.right:
                    return self.find(root.left, sum - root.val) or self.find(root.right, sum - root.val)
                else:
                    return self.find(root.left, sum - root.val)
            else:
                if root.right:
                    return self.find(root.right, sum - root.val)
                else:
                    return sum == root.val
