# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root) -> list:
        res, nodes = [], [root] if root else []
        while nodes:
            res.append(list(node.val for node in nodes))
            nodes = [x for node in nodes for x in (node.left, node.right) if x]
        res.reverse()
        return res


a = Solution()
b = a.levelOrderBottom([3, 9, 20, None, None, 15, 7])
print(b)
