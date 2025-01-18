#
# @lc app=leetcode.cn id=2958 lang=python3
#
# [2958] 最多 K 个重复元素的最长子数组
#
from preImport import *
# @lc code=start
class Solution:
    """
        Sliding window
    """
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, num in enumerate(nums): # 枚舉右端點
            cnt[num] += 1
            while cnt[num] > k: # 不符合條件，開始縮小窗口(移動左端點)
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1) # 此時 [left, right] 是符合條件的子陣列，更新答案
        return ans
# @lc code=end

