'''

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.find(s, t):
            return True
        
        return False
    
    def find(self, s, t):
        if not s:
            if not t:
                return True
            else:
                return False
        else:
            if self.same(s, t):
                return True
            if self.find(s.left, t):
                return True
            if self.find(s.right, t):
                return True
        return False
    
    def same(self, s, t):
        if not s:
            if not t:
                return True
            else:
                return False
        else:
            if not t:
                return False
            else:
                return s.val == t.val and self.same(s.left, t.left) and self.same(s.right, t.right)
