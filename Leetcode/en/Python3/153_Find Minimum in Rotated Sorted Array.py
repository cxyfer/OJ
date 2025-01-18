# @algorithm @lc id=153 lang=python3 
# @title find-minimum-in-rotated-sorted-array


from en.Python3.mod.preImport import *
# @test([3,4,5,1,2])=1
# @test([4,5,6,7,0,1,2])=0
# @test([11,13,15,17])=11
class Solution:
    """
        Binary Search
        一段遞增，或兩段遞增

        - 紅：在最小值左側
        - 藍：最小值本身或在最小值右側
    """
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-2 # [left, right] 由於 nums[n-1] 一定是藍色，所以右界為 n-2
        while left <= right: # 區間不為空
            mid = (left + right) // 2
            if nums[mid] < nums[-1]: # 藍色：不管是一段遞增還是兩段遞增，最小值是 mid 或在 mid 的左側，故 mid 不是最小值本身就是在最小值右側
                right = mid - 1
            else: # 紅色：只可能是兩段遞增，最小值一定在 mid 的右側，故 mid 在最小值左側
                left = mid + 1
        return nums[left]