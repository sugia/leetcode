'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        vec = [root]
        while len(vec) > 0:
            next_vec = []
            for idx in xrange(len(vec)):
                if vec[idx].left:
                    next_vec.append(vec[idx].left)
                if vec[idx].right:
                    next_vec.append(vec[idx].right)
            res.append(vec[-1].val)
            vec = next_vec
            
        return res
