#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res1 = [1] * n # from left to right
        res2 = [1] * n # from right to left
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                res1[i] = res1[i-1] + 1
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                res2[j] = res2[j+1] + 1
        return sum(max(res1[i], res2[i]) for i in range(n))
# @lc code=end
sol = Solution()
print(sol.candy([1,0,2])) # 5
print(sol.candy([1,2,2])) # 4

