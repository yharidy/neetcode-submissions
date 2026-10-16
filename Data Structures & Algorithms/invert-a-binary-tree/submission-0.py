# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invert(node: TreeNode | None):
            if node is None:
                return node
            l, r = node.left, node.right
            node.left, node.right = _invert(r), _invert(l)
            return node
        return _invert(root)
        
        