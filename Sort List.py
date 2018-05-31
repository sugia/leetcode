'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        fast, slow, slow_prev = head, head, None
        while fast and fast.next:
            fast, slow, slow_prev = fast.next.next, slow.next, slow
            
        slow_prev.next = None
        sorted_a = self.sortList(head)
        sorted_b = self.sortList(slow)
        
        return self.mergeLists(sorted_a, sorted_b)
    
    def mergeLists(self, a, b):
        dummy = ListNode(0)
        cur = dummy
        
        while a and b:
            if a.val < b.val:
                cur.next = a
                cur = cur.next
                a = a.next
            else:
                cur.next = b
                cur = cur.next
                b = b.next
                
        if a:
            cur.next = a
        if b:
            cur.next = b     
        
        return dummy.next
