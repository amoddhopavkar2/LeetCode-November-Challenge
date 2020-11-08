# Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: TreeNode, answer=True) -> int:
        if not root:
            return 0 if answer else (0, 0)
        left_sum, left_difference = self.findTilt(root.left, False)
        right_sum, right_difference = self.findTilt(root.right, False)
        
        result = abs(left_sum - right_sum) + left_difference + right_difference
        if not answer:
            result = root.val + left_sum + right_sum, result
        
        return result
        