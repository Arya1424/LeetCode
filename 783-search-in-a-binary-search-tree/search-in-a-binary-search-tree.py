# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        curr=root
        while curr:
            if not curr:
                return []
            if curr.val==val:
                return curr
            elif val>curr.val:
                curr=curr.right
            else:
                curr=curr.left
        
        