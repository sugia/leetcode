'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        num_fre = {}
        self.find(root, num_fre)
        
        for num in num_fre:
            y = k - num
            if y == num:
                if num_fre[num] > 1:
                    return True
            else:
                if y in num_fre:
                    return True
            
        return False
    
    def find(self, root, num_fre):
        if not root:
            return
        
        if root.val not in num_fre:
            num_fre[root.val] = 1
        else:
            num_fre[root.val] += 1
        self.find(root.left, num_fre)
        self.find(root.right, num_fre)
