# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        curr=head
        if not head or not head.next:
            return True
        
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        curr=slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        first,second=head,prev

        while second:
            if first.val != second.val:
                return False
            first=first.next
            second=second.next
        return True






        