# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        curr=head
        elems=[]
        while curr:
            elems.append(curr.val)
            curr=curr.next
        l,r=0,len(elems)-1
        max_twin=0
        while l<r:
            max_twin=max(max_twin,elems[l]+elems[r])
            l+=1
            r-=1
        return max_twin


        