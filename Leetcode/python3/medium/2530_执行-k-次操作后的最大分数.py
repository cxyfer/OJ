#
# @lc app=leetcode.cn id=2530 lang=python3
#
# [2530] 执行 K 次操作后的最大分数
#
from preImport import *
# @lc code=start
class Solution:
    """
        Greedy + Heap
    """
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        h = []
        for num in nums:
            heapq.heappush(h, -num)
        for _ in range(k):
            res = -heapq.heappop(h)
            ans += res
            heapq.heappush(h, -ceil(res/3))
        return ans
# @lc code=end
sol = Solution()
print(sol.maxKelements([10,10,10,10,10],5)) # 50
print(sol.maxKelements([1,10,3,3,3],3)) # 17