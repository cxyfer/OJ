# @algorithm @lc id=337 lang=python3 
# @title house-robber-iii


from en.Python3.mod.preImport import *
# @test([3,2,3,null,3,null,1])=7
# @test([3,4,5,1,3,null,1])=9
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        選擇根節點或不選擇根節點
        選擇根節點：左節點不選擇 + 右節點不選擇 + 根節點的值
        不選擇根節點: 左節點選擇或不選擇的最大值 + 右節點選擇或不選擇的最大值
    """
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            # select this node or not
            val1 = left[1] + right[1] + node.val
            val2 = max(left) + max(right)
            return [val1, val2]
        return max(dfs(root))  # 根节点选或不选的最大值