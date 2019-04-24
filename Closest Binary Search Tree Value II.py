'''
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

    Given target value is a floating point.
    You may assume k is always valid, that is: k ≤ total nodes.
    You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        h = []
        self.build(root, target, h)
        res = []
        for i in xrange(k):
            res.append(heapq.heappop(h)[1])
        return res
    def build(self, node, target, h):
        if not node:
            return
        heapq.heappush(h, [abs(node.val - target), node.val])
        self.build(node.left, target, h)
        self.build(node.right, target, h)
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        prev_list = self.getPrevList(root, target)
        next_list = self.getNextList(root, target)
        if prev_list and next_list and prev_list[-1] == next_list[-1]:
            self.getPrev(prev_list)
            
        res = []
        for _ in range(k):
            if prev_list:
                if next_list:
                    prev_diff = abs(prev_list[-1].val - target)
                    next_diff = abs(next_list[-1].val - target)
                    if prev_diff < next_diff:
                        res.append(self.getPrev(prev_list))
                    else:
                        res.append(self.getNext(next_list))
                else:
                    res.append(self.getPrev(prev_list))
            else:
                if next_list:
                    res.append(self.getNext(next_list))
                else:
                    break
        
        return res
    
    def getPrevList(self, node: TreeNode, target: int) -> List[TreeNode]:
        prev_list = []
        while node:
            if node.val == target:
                prev_list.append(node)
                break
            elif node.val < target:
                prev_list.append(node)
                node = node.right
            else:
                node = node.left
        return prev_list
    
    def getNextList(self, node: TreeNode, target: int) -> List[TreeNode]:
        next_list = []
        while node:
            if node.val == target:
                next_list.append(node)
                break
            elif node.val < target:
                node = node.right
            else:
                next_list.append(node)
                node = node.left
        return next_list
    
    def getPrev(self, prev_list: List[TreeNode]) -> int:
        node = prev_list.pop()
        res = node.val
        node = node.left
        while node:
            prev_list.append(node)
            node = node.right
        return res
    
    def getNext(self, next_list: List[TreeNode]) -> int:
        node = next_list.pop()
        res = node.val
        node = node.right
        while node:
            next_list.append(node)
            node = node.left
        return res
