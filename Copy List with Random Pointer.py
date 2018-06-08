'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.


'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        dic = {}
        cur = head
        while cur:
            if cur not in dic:
                mirror = RandomListNode(cur.label)
                dic[cur] = mirror
            
            if cur.next:
                if cur.next not in dic:
                    mirror = RandomListNode(cur.next.label)
                    dic[cur.next] = mirror
                    
                dic[cur].next = dic[cur.next]
                
            if cur.random:
                if cur.random not in dic:
                    mirror = RandomListNode(cur.random.label)
                    dic[cur.random] = mirror
                    
                dic[cur].random = dic[cur.random]
                
            cur = cur.next
            
        return dic[head]
