# @algorithm @lc id=437 lang=python3 
# @title path-sum-iii


from en.Python3.mod.preImport import *
# @test([10,5,-3,3,2,null,11,3,-2,null,1],8)=3
# @test([5,4,8,11,null,13,4,7,2,null,null,5,1],22)=3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        DFS，同時mantain一個紀錄不同長度的sum的sumList
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, sumList):
            if not node:
                return 0
            sumList = [num + node.val for num in sumList] + [node.val]
            count = sum([1 for num in sumList if num == targetSum])
            return count + dfs(node.left, sumList) + dfs(node.right, sumList)
        ans = dfs(root, [])
        return ans