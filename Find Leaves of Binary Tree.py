'''
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree

          1
         / \
        2   3
       / \     
      4   5    

Returns [4, 5, 3], [2], [1].

Explanation:

1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         / 
        2          

2. Now removing the leaf [2] would result in this tree:

          1          

3. Now removing the leaf [1] would result in the empty tree:

          []         

Returns [4, 5, 3], [2], [1].

Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        
        dic = {}
        self.build(root, dic)
        
        for key in xrange(max(dic.keys())+1):
            res.append(dic[key])
        return res
        
    def build(self, node, dic):
        if not node:
            return -1
        
        if node.left:
            left_high = self.build(node.left, dic)
            if node.right:
                right_high = self.build(node.right, dic)
                
                high = max(left_high, right_high) + 1
            else:
                high = left_high + 1
        else:
            if node.right:
                right_high = self.build(node.right, dic)
                high = right_high + 1
            else:
                high = 0
                
        if high in dic:
            dic[high].append(node.val)
        else:
            dic[high] = [node.val]
                
        return high
