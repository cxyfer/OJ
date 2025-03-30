#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    # Sliding window, two pointers (同向雙指標)
     - Similar to 209. Minimum Size Subarray Sum
"""
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 目標是找乘積小於 k 的子陣列，如果 k <= 1，則需要乘積 < 1，但所有數字都 >= 1，因此無解
        if k <= 1: 
            return 0
        ans = left = 0
        prod = 1
        for right, x in enumerate(nums): # 枚舉右端點
            prod *= x
            while prod >= k: # 不符合條件，開始縮小窗口(移動左端點)
                prod /= nums[left]
                left += 1
            # 此時 [left, right] 是符合條件的子陣列
            # 在固定右端點的情況下，左端點可以在 [left, right] 之間選擇，故總共有 right-left+1 種子陣列
            ans += (right - left + 1)
        return ans
# @lc code=end

