#
# @lc app=leetcode id=2461 lang=python3
# @lcpr version=30204
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        left = s = have = ans = 0
        for right, x in enumerate(nums):
            # 1. 入窗口
            cnt[x] += 1
            s += x
            if cnt[x] == 1:
                have += 1
            if right < k - 1:
                continue
            # 2. 更新答案
            if have == k:
                ans = max(ans, s)
            # 3. 出窗口
            cnt[nums[left]] -= 1
            s -= nums[left]
            if cnt[nums[left]] == 0:
                have -= 1
            left += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.maximumSubarraySum([1,5,4,2,9,9,9], 3)) # 15
print(sol.maximumSubarraySum([4,4,4], 3)) # 0

#
# @lcpr case=start
# [1,5,4,2,9,9,9]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4,4,4]\n3\n
# @lcpr case=end

#

