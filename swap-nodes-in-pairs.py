'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution:
    #given a list node
    #return a list node
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p and p.next and p.next.next:
            q = p.next
            nex = p.next
            p.next = q.next
            q.next = p.next.next
            p.next.next = nex
            p = q
        return dummy.next
