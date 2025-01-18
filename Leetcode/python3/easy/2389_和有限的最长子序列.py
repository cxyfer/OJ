#
# @lc app=leetcode.cn id=2389 lang=python3
#
# [2389] 和有限的最长子序列
#
from preImport import *
# @lc code=start
class Solution:
    """
        Prefix Sum + Binary Search
    """
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        nums.sort()
        s = [0] * (n + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        ans = [0] * m
        for i, q in enumerate(queries):
            idx = bisect_right(s, q)
            ans[i] = idx - 1
        return ans
# @lc code=end
sol = Solution()
# @test([4,5,2,1],[3,10,21])=[2,3,4]
# @test([2,3,4,5],[1])=[0]
print(sol.answerQueries([4,5,2,1],[3,10,21])) #[2,3,4]
print(sol.answerQueries([2,3,4,5],[1])) #[0]
