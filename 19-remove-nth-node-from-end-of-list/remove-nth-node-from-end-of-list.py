class Solution(object):
    def removeNthFromEnd(self, head, n):
        # First pass: count the length
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # If need to remove the head
        if n == length:
            return head.next
        
        # Find the node before the one to delete
        current = head
        for _ in range(length - n - 1):
            current = current.next
        
        # Remove the nth node from the end
        current.next = current.next.next
        
        return head
