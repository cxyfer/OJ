#
# @lc app=leetcode.cn id=1425 lang=python3
#
# [1425] 带限制的子序列和
#
from preImport import *
# @lc code=start
class Solution:
    """
        Dynamic Programming + Monotonic Queue
    """
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        q = deque()
        q.append(0)
        ans = nums[0]
        for i in range(1, n):
            while q and i - q[0] > k: # pop the out-of-range index
                q.popleft()
            dp[i] = max(nums[i], nums[i] + dp[q[0]])
            ans = max(ans, dp[i])
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
        return ans
# @lc code=end

