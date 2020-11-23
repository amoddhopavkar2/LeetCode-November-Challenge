# House Robber III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root: TreeNode) -> tuple:
    rob_me = 0
    rob_children = 0

    if root.right is not None:
        child_robbed, child_not_robbed = solve(root.right)
        rob_children += max(child_robbed, child_not_robbed)
        rob_me += child_not_robbed

    if root.left is not None:
        child_robbed, child_not_robbed = solve(root.left)
        rob_children += max(child_robbed, child_not_robbed)
        rob_me += child_not_robbed

    rob_me += root.val

    return rob_me, rob_children

class Solution:

    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0

        a, b = solve(root)
        return max(a, b)
    