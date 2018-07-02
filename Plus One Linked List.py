'''
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:

Input:
1->2->3

Output:
1->2->4

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = 0
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next:
            cur = cur.next
            tmp = tmp * 10 + cur.val
            
        tmp += 1
        data = []
        while tmp > 0:
            data.append(tmp % 10)
            tmp //= 10
            
        cur = dummy
        for x in reversed(data):
            nex = ListNode(x)
            cur.next = nex
            cur = cur.next
            
        return dummy.next
