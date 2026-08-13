# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def lenOfLL(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        
        len_ = 0
        itr = head
        while itr:
            len_ += 1
            itr = itr.next
        return len_

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Handle empty list or single-node list
        n = self.lenOfLL(head)
        if n <= 1:
            return head
        
        # 2. Optimize k and check if rotation is even needed
        new_k = k % n
        if new_k == 0:
            return head
        
        # 3. Find the node right before the new head
        tar = 1
        itr = head
        while tar != (n - new_k):
            itr = itr.next
            tar += 1
            
        # 4. Break the link and reconnect the tail to the old head
        new_head = itr.next
        itr.next = None
        
        itr2 = new_head
        while itr2.next:
            itr2 = itr2.next
            
        itr2.next = head
        return new_head
