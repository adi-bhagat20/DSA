# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        if length == n:
            return head.next
        
        count = 0
        temp = head
        while count != length - n - 1:
            count += 1
            temp = temp.next
        
        temp.next = temp.next.next
        return head