#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Greedy
為了找到 (nums[i] - nums[j]) * nums[k] 的最大值
基於貪心思路，可以使 (nums[i] - nums[j]) 和 nums[k] 越大越好
由於需要滿足 i < j < k，所以又有兩種思路

1. 枚舉 nums[j]，然後找最大的 nums[i] 和 nums[k]，可以透過前後綴分解實現
2. 枚舉 nums[k]，維護前綴中的最大差值 (nums[i] - nums[j])，並維護前綴中最大的 nums[i] 以更新最大差值
"""
# @lc code=start
class Solution1:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]  # 後綴最大值
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i + 1], nums[i])
        ans = 0
        pre_mx = nums[0]  # 前綴最大值
        for i in range(1, n - 1):
            ans = max(ans, (pre_mx - nums[i]) * suf[i + 1])
            pre_mx = max(pre_mx, nums[i])
        return ans

class Solution2:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        mx = mx_diff = float('-inf')
        for x in nums:
            ans = max(ans, mx_diff * x)
            mx_diff = max(mx_diff, mx - x)  # (nums[i] - nums[j])
            mx = max(mx, x)  # nums[i]
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

