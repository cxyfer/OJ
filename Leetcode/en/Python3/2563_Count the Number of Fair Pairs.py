# @algorithm @lc id=2699 lang=python3 
# @title count-the-number-of-fair-pairs


from en.Python3.mod.preImport import *
# @test([0,1,7,4,4,5],3,6)=6
# @test([1,7,9,2,5],11,11)=1
class Solution:
    """
        Binary Search
        由於順序不影響Fair Pairs的對數，所以可以先對nums進行排序，
        然後對於每個數字nums[i]，在nums中找到最大的j使得nums[j] - nums[i] <= upper，
    """
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for idx, x in enumerate(nums):
            l = bisect_left(nums, lower - x, 0, idx) # (arr, x, lo=0, hi=idx)
            r = bisect_right(nums, upper - x, 0, idx)
            ans += r - l # 取 l 到 r-1 之間的數都能和 x 組成Fair Pair，
        return ans