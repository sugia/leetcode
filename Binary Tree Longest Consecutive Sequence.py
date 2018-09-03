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
        res = 0
        if not root:
            return res
        vec = [(root, 1)]
        while vec:
            node, length = vec.pop()
            res = max(res, length)
            if node.left:
                if node.left.val == node.val + 1:
                    vec.append((node.left, length+1))
                else:
                    vec.append((node.left, 1))
            if node.right:
                if node.right.val == node.val + 1:
                    vec.append((node.right, length+1))
                else:
                    vec.append((node.right, 1))
        return res
            
