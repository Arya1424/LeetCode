# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        i=j=1
        num1=num2=0
        while l1:
            num1+=l1.val*i
            i=i*10
            l1=l1.next
        while l2:
            num2+=l2.val*j
            j=j*10
            l2=l2.next
        tot=num1+num2
        if tot==0:
            return ListNode(0)

        head=ListNode()
        curr=head
        while tot>0:
            digit=tot%10
            curr.val=digit
            tot=tot//10
            if tot>0:
                curr.next=ListNode()
                curr=curr.next

        return head


        