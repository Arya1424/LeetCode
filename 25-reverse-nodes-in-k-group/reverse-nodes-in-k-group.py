# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k==1:
            return head
        count=0
        dummy=ListNode(0)
        dummy.next=head
        current=head
        prev=dummy

        while current:
            current=current.next
            count+=1

        while count>=k:
            current=prev.next
            nxt=current.next

            for i in range(k-1):
                current.next=nxt.next
                nxt.next=prev.next
                prev.next=nxt
                nxt=current.next
            prev=current
            count-=k

        return dummy.next


