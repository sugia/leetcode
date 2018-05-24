'''

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return -1
        heap = []
        vec = [root]
        while len(vec) > 0:
            next_vec = []
            for node in vec:
                heapq.heappush(heap, node.val)
                if node.left:
                    next_vec.append(node.left)
                if node.right:
                    next_vec.append(node.right)
            vec = next_vec
        res = -1
        for i in xrange(k):
            res = heapq.heappop(heap)
            
        return res
