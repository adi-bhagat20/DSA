# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lenOfLL(self , head):
        if not head:
            return 0

        itr = head
        len_ = 0

        while itr:
            len_ += 1
            itr = itr.next
        
        return len_

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.lenOfLL(head)
        if n <= 1:
            return head

        new_k = k%n
        if new_k==0:
            return head

        tar = 1
        itr = head
        while tar != (n - new_k):
            itr = itr.next
            tar += 1
        
        new_head = itr.next
        itr.next = None

        itr2 = new_head
        while itr2.next:
            itr2 = itr2.next
        
        itr2.next = head

        return new_head