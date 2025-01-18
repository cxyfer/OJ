#
# @lc app=leetcode.cn id=100033 lang=python3
#
# [100033] 最大合金数
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Binary search
    """
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ans = 0
        mx = min(stock) + budget # 最多能做幾個

        for com in composition:
            def check(num):
                spend = 0
                for need, s, c in zip(com, stock, cost): # 檢查每種材料
                    spend += (need * num - s) * c if s < need * num else 0
                    if spend > budget:
                        return False
                return True

            left, right = 0, mx + 1 # 左閉右開 [left, right)
            while left < right - 1: # 左閉右開 [left, right)
                mid = (left + right) // 2
                if check(mid):
                    left = mid
                else:
                    right = mid
            ans = max(ans, left) # 更新答案
        return ans
# @lc code=end

