'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.


'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start:
            end = start
            for i in xrange(k):
                end = end.next
                if not end:
                    return dummy.next
            next_start = start.next
            self.reverse(start, k)
            start = next_start
            
        return dummy.next
    
    def debug(self, dummy):
        cur = dummy
        while cur:
            print cur.val,
            cur = cur.next
        print
        
    def reverse(self, start, k):
        nex = start.next
        r = start.next.next
        for i in xrange(1, k):
            start.next, r.next, nex.next, r = r, start.next, r.next, r.next
