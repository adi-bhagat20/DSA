# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # STEP 1: Insert cloned nodes next to originals
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
            
        # STEP 2: Copy random pointers
        curr = head
        while curr:
            if curr.random:
                # The copy node's random points to the original node's random's copy
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # STEP 3: Separate the interleaved lists
        curr = head
        dummy = Node(0)
        copy_curr = dummy
        
        while curr:
            # Isolate the copy node
            copy_curr.next = curr.next
            copy_curr = copy_curr.next
            
            # Restore the original node's link
            curr.next = copy_curr.next
            curr = curr.next
            
        return dummy.next
