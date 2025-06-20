# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        index=[0]
        def helper(bound):
            if index[0]==len(preorder) or preorder[index[0]]>bound:
                return None
            root_val=preorder[index[0]]
            index[0]+=1
            root=TreeNode(root_val)

            root.left=helper(root_val)
            root.right=helper(bound)

            return root
        return helper(float('inf'))