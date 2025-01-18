#
# @lc app=leetcode.cn id=823 lang=python3
#
# [823] 带因子的二叉树
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        idx = {x: i for i, x in enumerate(arr)} # 用字典保存每個數的下標
        @cache # 避免重複計算相同的結果
        def dfs(i: int) -> int: # 以 arr[i] 為根的Binary Tree的數量
            res = 1
            val = arr[i] # 當前節點的值
            for j in range(i): # 檢查比當前節點值小的數
                x = arr[j]
                # x 可以作為當前節點的左子樹，且val // x為右子樹的值，也存在於arr中 (用idx這個雜湊表查詢)
                if val % x == 0 and val // x in idx:
                    res += dfs(j) * dfs(idx[val // x]) # 左子樹數量 * 右子樹數量
            return res
        return sum(dfs(i) for i in range(n)) % (10**9 + 7)
# @lc code=end

sol = Solution()
print(sol.numFactoredBinaryTrees([2,4,5,10])) # 7
print(sol.numFactoredBinaryTrees([2,4])) # 3


