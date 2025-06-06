# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = [root]  # queue to track nodes at each level
        
        while queue:
            level = []
            next_queue = []
            
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            result.append(level)
            queue = next_queue  # move to next level
        
        return result
