#
# @lc app=leetcode id=3434 lang=python3
# @lcpr version=30204
#
# [3434] Maximum Frequency After Subarray Operation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        # 枚舉 tgt = k - x，找到貢獻最大的子陣列 (Maximum Subarray Sum)
        for tgt in range(1, 51):
            if tgt == k:
                continue
            D = [0] * n
            for i, v in enumerate(nums):
                if v == tgt:  # 加 x 後能變成 k，增加貢獻
                    D[i] = 1
                elif v == k:  # 本來就是 k，加 x 後會減少貢獻
                    D[i] = -1
            # 前綴和求最大子陣列和
            s = mn = 0
            for d in D:
                s += d
                ans = max(ans, s - mn)
                mn = min(mn, s)
        return nums.count(k) + ans
# @lc code=end

sol = Solution()
print(sol.maxFrequency([1,2,3,4,5,6], 1)) # 2
print(sol.maxFrequency([10,2,3,4,5,5,4,3,2,2], 10)) # 4
print(sol.maxFrequency([2,3,7,1,7], 7)) # 4

#
# @lcpr case=start
# [1,2,3,4,5,6]\n1\n
# @lcpr case=end

# @lcpr case=start
# [10,2,3,4,5,5,4,3,2,2]\n10\n
# @lcpr case=end

#

