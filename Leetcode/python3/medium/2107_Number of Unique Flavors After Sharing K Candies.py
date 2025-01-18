#
# @lc app=leetcode id=2107 lang=python3
# @lcpr version=30204
#
# [2107] Number of Unique Flavors After Sharing K Candies
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        cnt = Counter(candies)
        if k == 0:
            return len(cnt)
        ans = 0
        left = 0
        for right, x in enumerate(candies):
            cnt[x] -= 1
            if cnt[x] == 0:
                del cnt[x]
            if right - left + 1 < k:
                continue
            ans = max(ans, len(cnt))
            cnt[candies[left]] += 1
            left += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.shareCandies([1,2,2,3,4,3], 3)) # 3
print(sol.shareCandies([2,2,2,2,3,3], 2)) # 2
print(sol.shareCandies([2,4,5], 0)) # 3
print(sol.shareCandies([1,1,2,1], 2)) # 2
#
# @lcpr case=start
# [1,2,2,3,4,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,3,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,4,5]\n0\n
# @lcpr case=end

#

