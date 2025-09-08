# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        def helper(node,count,isLeft):
            if not node: return count
            if isLeft:
                count=max(count,helper(node.right,count+1,False),helper(node.left,0,True))
            else:
                count=max(count,helper(node.right,0,False),helper(node.left,count+1,True))
            return count
        return max(helper(root.left,0,True),helper(root.right,0,False))
        