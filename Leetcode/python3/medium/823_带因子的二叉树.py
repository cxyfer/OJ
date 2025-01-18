#
# @lc app=leetcode.cn id=823 lang=python3
#
# [823] 带因子的二叉树
#
from preImport import *
# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        arr.sort()
        idxs = {x:idx for idx, x in enumerate(arr)} # 用字典保存每個數的下標
        @cache # 避免重複計算相同的結果
        def dfs(i: int) -> int: # 以 arr[i] 為root的Binary Tree的數量
            res = 1
            val = arr[i] # 當前節點的值
            for j in range(i): # 檢查比當前節點值小的數
                x = arr[j]
                # x 可以作為當前節點的左子樹，且val // x為右子樹的值，也存在於arr中 (用idxs這個雜湊表查詢)
                if val % x == 0 and val // x in idxs:
                    res += dfs(j) * dfs(idxs[val // x]) # 左子樹數量 * 右子樹數量
            return res
        return sum(dfs(i) for i in range(n)) % MOD
# @lc code=end

