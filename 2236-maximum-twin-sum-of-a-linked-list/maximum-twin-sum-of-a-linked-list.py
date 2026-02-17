# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        head_sec=slow
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        maxSum=head.val+prev.val
        while prev and head:
            maxSum=max(maxSum, prev.val+head.val)
            head=head.next
            prev=prev.next
        return maxSum