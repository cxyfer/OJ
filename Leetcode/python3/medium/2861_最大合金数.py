#
# @lc app=leetcode.cn id=2861 lang=python3
#
# [2861] 最大合金数
#
from preImport import *
# @lc code=start
class Solution:
    """
        Binary search

        注意循環不變量：
        - left - 1 的回答一定為「是」
        - right + 1 的回答一定為「否」
    """
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ans = 0
        mx = min(stock) + budget # 最多能做幾個

        for com in composition: # 只能使用一台機器，所以對這台機器能做的最大數量進行二分

            def check(num):
                spend = 0
                for need, s, c in zip(com, stock, cost): # 檢查每種材料
                    spend += max(0, need * num - s) * c
                    if spend > budget:
                        return False
                return True

            left, right = 0, mx # [left, right]
            while left <= right: # 區間不為空
                mid = (left + right) // 2
                if check(mid): # 詢問：能否用出 mid 個合金？
                    left = mid + 1
                else:
                    right = mid - 1
            ans = max(ans, right) # 更新答案, or left-1
        return ans
# @lc code=end

