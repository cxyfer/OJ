#
# @lc app=leetcode id=862 lang=python3
# @lcpr version=30204
#
# [862] Shortest Subarray with Sum at Least K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Similar
- 209. Minimum Size Subarray Sum - 全正數版本的本題，可以用雙指標維護，相對簡單許多
- P1714 切蛋糕
- 3938. Maximum Path Intersection Sum in a Grid
"""
# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial = 0))

        ans = n + 1
        q = deque()
        for r, sr in enumerate(s):
            while q and sr - s[q[0]] >= k:
                ans = min(ans, r - q[0])
                q.popleft()
            
            while q and sr <= s[q[-1]]:
                q.pop()

            q.append(r)

        return ans if ans <= n else -1
# @lc code=end

sol = Solution()
print(sol.shortestSubarray([1], 1)) # 1
print(sol.shortestSubarray([1,2], 4)) # 1
print(sol.shortestSubarray([2,-1,2], 3)) # -1

#
# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,2]\n3\n
# @lcpr case=end

#

