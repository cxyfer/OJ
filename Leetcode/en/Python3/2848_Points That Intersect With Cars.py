# @algorithm @lc id=3034 lang=python3 
# @title points-that-intersect-with-cars


from mod.preImport import *
# @test([[3,6],[1,5],[4,7]])=7
# @test([[1,3],[5,8]])=7
class Solution:
    """
        Similar to 56. Merge Intervals
    """
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        ans = []
        for x, y in nums:
            if not ans or x > ans[-1][1]: # not overlap
                ans.append([x, y])
            else:
                ans[-1][1] = max(ans[-1][1], y) # overlap, update interval
        return sum([y - x + 1 for x, y in ans])
    
sol = Solution()
print(sol.numberOfPoints([[3,6],[1,5],[4,7]])) # 7
print(sol.numberOfPoints([[1,3],[5,8]])) # 7