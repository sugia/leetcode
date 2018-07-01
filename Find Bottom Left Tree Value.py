'''
 Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL. 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        
        vec = [root]
        while vec:
            next_vec = []
            for node in vec:
                if node.left:
                    next_vec.append(node.left)
                if node.right:
                    next_vec.append(node.right)
            
            if next_vec:
                vec = next_vec
            else:
                return vec[0].val
            
        return -1
