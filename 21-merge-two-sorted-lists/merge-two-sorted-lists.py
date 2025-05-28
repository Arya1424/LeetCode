# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        value1=list1
        value2=list2
        while value1 is not None and value2 is not None:
            if value1.val<value2.val:
                current.next=ListNode(value1.val)
                value1=value1.next
                current=current.next
            else:
                current.next=ListNode(value2.val)
                value2=value2.next
                current=current.next

        while value1 is not None:
            current.next=ListNode(value1.val)
            value1=value1.next
            current=current.next

        while value2 is not None:
            current.next=ListNode(value2.val)
            value2=value2.next
            current=current.next

        return head.next