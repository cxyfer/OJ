# @algorithm @lc id=1568 lang=python3 
# @title pseudo-palindromic-paths-in-a-binary-tree


from en.Python3.mod.preImport import *
# @test([2,3,1,3,1,null,1])=2
# @test([2,1,1,1,3,null,null,null,null,null,1])=1
# @test([9])=1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        cnt = Counter()
        def dfs(root):
            if not root:
                return 0
            cnt[root.val] += 1
            if not root.left and not root.right: # leaf
                tmp = 0
                for v in cnt.values():
                    if v % 2 != 0:
                        tmp += 1
                cnt[root.val] -= 1
                return 1 if tmp <= 1 else 0 # 奇數個數最多只能有一個
            ans = dfs(root.left) + dfs(root.right)
            cnt[root.val] -= 1
            return ans
        
        return dfs(root)