# @algorithm @lc id=501 lang=python3 
# @title find-mode-in-binary-search-tree


from en.Python3.mod.preImport import *
# @test([1,null,2,2])=[2]
# @test([0])=[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        不使用额外空间的方法：利用BST的中序遍历是有序的特性
    """
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        base, cnt, maxCnt = 0, 0, 0

        def update(x):
            nonlocal ans, base, cnt, maxCnt
            if x == base:
                cnt += 1
            else:
                cnt = 1
                base = x
            if cnt == maxCnt:
                ans.append(base)
            if cnt > maxCnt:
                maxCnt = cnt
                ans = [base]

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            update(root.val)
            dfs(root.right)

        dfs(root)
        return ans
