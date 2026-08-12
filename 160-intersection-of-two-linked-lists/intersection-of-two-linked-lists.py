# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()

        itr = headA
        while itr:
            s.add(itr)
            itr = itr.next
        
        itr = headB
        while itr:
            if itr in s:
                return itr
            itr = itr.next
        
        return None