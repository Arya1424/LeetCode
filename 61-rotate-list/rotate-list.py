# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or not k:
            return head
        
        length=1
        curr=head
        while curr.next:
            curr=curr.next
            length+=1
        k=k%length
        if k==0:
            return head
        curr.next=head

        steps=length-k
        newtail=head
        for i in range(steps-1):
            newtail=newtail.next
        head=newtail.next
        newtail.next=None
        return head