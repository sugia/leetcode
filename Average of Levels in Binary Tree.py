'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        vec = [root]
        while len(vec) > 0:
            total = 0
            next_vec = []
            for node in vec:
                total += node.val
                if node.left:
                    next_vec.append(node.left)
                if node.right:
                    next_vec.append(node.right)
            res.append(1.0 * total / len(vec))
            vec = next_vec
        return res
