#
# @lc app=leetcode.cn id=1561 lang=python3
#
# [1561] 你可以获得的最大硬币数目
#
from preImport import *
# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort(reverse=True)
        ans = 0
        for i in range(n):
            ans += piles[2*i+1]
        return ans
# @lc code=end

sol = Solution()
print(sol.maxCoins([2,4,1,2,7,8])) # 9
print(sol.maxCoins([2,4,5])) # 4
print(sol.maxCoins([9,8,7,6,5,1,2,3,4])) # 18
print(sol.maxCoins([2,4,1,2,7,8])) # 9
