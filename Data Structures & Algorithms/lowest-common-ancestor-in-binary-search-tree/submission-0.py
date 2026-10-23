# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p==q:
            return p
        if not p or not q:
            return None
        higher = p if p.val > q.val else q
        lower = q if higher==p else p
        if higher.val >= root.val and lower.val <= root.val:
            return root
        next = root.left if higher.val < root.val else root.right
        return self.lowestCommonAncestor(next, p, q)