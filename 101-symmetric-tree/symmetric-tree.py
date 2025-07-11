# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def sym(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val!=r.val:
                return False
            return sym(l.left,r.right) and sym(l.right,r.left)
        return sym(root.left,root.right)

        