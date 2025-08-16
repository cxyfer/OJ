#
# @lc app=leetcode id=1553 lang=python3
# @lcpr version=30201
#
# [1553] Minimum Number of Days to Eat N Oranges
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
DP
考慮三種情況：
1. 今天吃 1 個，明天吃 n-1 個
2. 若 n % 2 == 0，今天吃 n//2 個，明天吃 n//2 個
3. 若 n % 3 == 0，今天吃 2n//3 個，明天吃 n//3 個
Time complexity: O(n)

但由於 n 的範圍很大， O(n) 的時間複雜度會超時，因此可以去除第一種情況，只考慮後兩種情況：
1. 若 n % 2 == 1，則今天吃 1 個，明天就可以吃 n//2 個，剩下 n//2 個遞迴
    即需要吃 n % 2 + 1 + dfs(n // 2) 天
2. 若 n % 3 == 1, 2 ，則連續 1/2 天吃 1 個，再來吃 2n//3 個，剩下 n//3 個遞迴
    即需要吃 n % 3 + 1 + dfs(n // 3) 天
Time complexity: O(log n)
"""
# @lc code=start
class Solution:
    @cache
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))
# @lc code=end
sol = Solution()
print(sol.minDays(10)) # 4
print(sol.minDays(6)) # 3
print(sol.minDays(1)) # 1
print(sol.minDays(56)) # 6


#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 6\n
# @lcpr case=end

#

