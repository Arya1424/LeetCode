# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        visited=set()
        current=head
        while current is not None:
            if current in visited:
                return True
            visited.add(current)
            current=current.next
        return False