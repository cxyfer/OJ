#
# @lc app=leetcode id=3578 lang=python3
#
# [3578] Count Partitions With Max-Min Difference at Most K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9+7)
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        f[0] = s = 1
        q_mn, q_mx = deque(), deque()
        left = 0
        for i, x in enumerate(nums):
            while q_mn and q_mn[-1][1] >= x:
                q_mn.pop()
            while q_mx and q_mx[-1][1] <= x:
                q_mx.pop()
            q_mn.append((i, x))
            q_mx.append((i, x))

            while q_mx[0][1] - q_mn[0][1] > k:
                s = (s - f[left]) % MOD
                left += 1
                while left > q_mx[0][0]:
                    q_mx.popleft()
                while left > q_mn[0][0]:
                    q_mn.popleft()
            f[i + 1] = s
            s = (s + f[i + 1]) % MOD
        return f[n]
# @lc code=end

sol = Solution()
print(sol.countPartitions([9,4,1,3,7], 4))  # 6
print(sol.countPartitions([1,2,8], 2))  # 2