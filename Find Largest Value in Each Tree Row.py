'''
You need to find the largest value in each row of a binary tree.

Example:

Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        
        vec = [root]
        while vec:
            next_vec = []
            vec_max = float('-inf')
            for x in vec:
                vec_max = max(vec_max, x.val)
                if x.left:
                    next_vec.append(x.left)
                if x.right:
                    next_vec.append(x.right)
                    
            res.append(vec_max)
            vec = next_vec
            
        return res
                
