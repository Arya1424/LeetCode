# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev = dummy

        while current:
            if current.val == val:
                prev.next = current.next
                # no need for current.next = None
            else:
                prev = current
            current = current.next

        return dummy.next
