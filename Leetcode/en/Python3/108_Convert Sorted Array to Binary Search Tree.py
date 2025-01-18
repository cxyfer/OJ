# @algorithm @lc id=108 lang=python3 
# @title convert-sorted-array-to-binary-search-tree


from en.Python3.mod.preImport import *
# @test([-10,-3,0,5,9])=[0,-3,9,-10,null,5]
# @test([1,3])=[3,1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0: return None
        if n == 1: return TreeNode(nums[0])
        mid = n // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node