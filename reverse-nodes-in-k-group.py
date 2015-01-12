'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''

class Solution:
    #given a list node and an integer
    #return a list node
    def reverseKGroup(self, head, k):
        if head == None or head.next == None or k <= 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while True:
            q = p
            for i in range(k):
                if q.next:
                    q = q.next
                else:
                    return dummy.next
            q = p.next
            for i in range(k-1):
                nex = p.next
                p.next = q.next
                q.next = p.next.next
                p.next.next = nex
            p = q
        return dummy.next
