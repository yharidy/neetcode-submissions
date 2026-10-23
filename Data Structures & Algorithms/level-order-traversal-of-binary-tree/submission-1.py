# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #     stack = [[root]]
    #     res = [[root.val]]
    #     while stack:
    #         nodes = stack.pop(-1)
    #         children = []
    #         for node in nodes:
    #             if node.left:
    #                 children.append(node.left)
    #             if node.right:
    #                 children.append(node.right)
    #         if children:
    #             stack.append(children)
    #             res.append([x.val for x in children])
    #     return res

    # DFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth==len(res):
                # first node in this level
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return res
            
