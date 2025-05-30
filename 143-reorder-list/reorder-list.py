# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # Step 1: Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        current = slow.next
        slow.next = None  # split the list into two
        while current:
            after = current.next
            current.next = prev
            prev = current
            current = after

        # Step 3: Merge two halves
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        return head
