# @algorithm @lc id=2469 lang=python3 
# @title longest-subsequence-with-limited-sum


from en.Python3.mod.preImport import *
# @test([4,5,2,1],[3,10,21])=[2,3,4]
# @test([2,3,4,5],[1])=[0]
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