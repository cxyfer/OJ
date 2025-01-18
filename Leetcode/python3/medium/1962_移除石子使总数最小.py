#
# @lc app=leetcode.cn id=1962 lang=python3
#
# [1962] 移除石子使总数最小
#
from preImport import *
# @lc code=start
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        hp = [-x for x in piles]
        heapify(hp)
        for _ in range(k):
            x = -heappop(hp)
            heappush(hp, -(x - x // 2))
        return -sum(hp)
# @lc code=end
sol = Solution()
print(sol.minStoneSum([5,4,9],2)) # 12
print(sol.minStoneSum([4,3,6,7],3)) # 12