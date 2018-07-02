'''
 Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer. 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        fre = {}
        
        self.find(root, fre)
        
        max_fre = max(fre.values())
        res = []
        for k, v in fre.iteritems():
            if v == max_fre:
                res.append(k)
                
        return res
    
    def find(self, node, fre):
        '''
        :type node: TreeNode
        :type fre: Dictionary
        :rtype: int
        '''
        
        if not node:
            return 0
        
        left = self.find(node.left, fre)
        right = self.find(node.right, fre)
        
        tmp = node.val + left + right
        if tmp in fre:
            fre[tmp] += 1
        else:
            fre[tmp] = 1
            
        return tmp
