'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution:
    #given a list of list node
    #return a list node
    def mergeKLists(self, lists):
        heap = []
        for x in lists:
            if x:
                heapq.heappush(heap, [x.val, x])
        dummy = ListNode(0)
        p = dummy
        while len(heap) > 0:
            q = heapq.heappop(heap)[1]
            p.next = q
            p = p.next
            if q.next:
                heapq.heappush(heap, [q.next.val, q.next])
        return dummy.next
