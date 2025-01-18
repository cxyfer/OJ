#
# @lc app=leetcode id=862 lang=python3
# @lcpr version=30204
#
# [862] Shortest Subarray with Sum at Least K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        

        q = deque()
        ans = n + 1
        for j in range(n + 1):
            while q and s[j] - s[q[0]] >= k:
                ans = min(ans, j - q[0])
                q.popleft()
            
            while q and s[j] <= s[q[-1]]:
                q.pop()
            
            q.append(j)
        
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

