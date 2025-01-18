#
# @lc app=leetcode id=1103 lang=python3
# @lcpr version=30203
#
# [1103] Distribute Candies to People
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        ans = [0] * n
        i = 0
        while candies > 0: # 第 i 次分配 i + 1 顆糖果給第 i % n 個人
            ans[i % n] += min(candies, i + 1) 
            candies -= i + 1
            i += 1
        return ans
"""
    1 + 2 + ... + m = m * (m + 1) / 2 <= candies
    -> m^2 + m <= 2 * candies -> m^2 + m - 2 * candies <= 0 -> m <= (-1 + sqrt(1 + 8 * candies)) / 2
"""
class Solution2:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        m = int((-1 + sqrt(8 * candies + 1)) / 2) # 可以分配 m 次
        q, r = divmod(m, n) # 可以完整分配 q 輪，剩下 r 個
        ans = [0] * n
        for i in range(n):
            ans[i] =  q * (q - 1) // 2 * n + q * (i + 1)
            if i < r:
                ans[i] += q * n + i + 1
            elif i == r:
                ans[i] += candies - m * (m + 1) // 2
        return ans

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# 7\n4\n
# @lcpr case=end

# @lcpr case=start
# 10\n3\n
# @lcpr case=end

#

