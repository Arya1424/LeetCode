# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        fast=slow=head
        prev=None
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        prev.next=slow.next
        return head
