# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(a, b):
            q = deque([(a,b)])
            while q:
                x, y = q.popleft()
                if not x and not y:
                    continue
                if not x or not y or x.val!=y.val:
                    return False
                q.append((x.left, y.left))
                q.append((x.right, y.right))
            return True
        queue = deque([root])
        while queue:
            root_node = queue.popleft()
            if not root_node:
                continue
            if root_node.val==subRoot.val and sameTree(root_node, subRoot):
                return True
            queue.append(root_node.left)
            queue.append(root_node.right)
        return False