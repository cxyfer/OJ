# @algorithm @lc id=154 lang=python3 
# @title find-minimum-in-rotated-sorted-array-ii


from en.Python3.mod.preImport import *
# @test([1,3,5])=1
# @test([2,2,2,0,1])=0
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        # return self.solve2a(nums)
        return self.solve2b(nums)
    """
        2a. Binary Search
        和 153. Find Minimum in Rotated Sorted Array 相比，需要考慮重複元素
        若二分時遇到重複元素，則將右界左移一位，直到不再遇到重複元素，即標註為藍色

        - 紅：在最小值左側
        - 藍：最小值本身或在最小值右側
    """
    def solve2a(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-2 # [left, right] 由於 nums[n-1] 一定是藍色，所以右界為 n-2
        while left <= right: # 區間不為空
            mid = (left + right) // 2
            if nums[mid] < nums[right+1]: # 藍色：mid 不是最小值本身就是在最小值右側
                right = mid - 1
            elif nums[mid] > nums[right+1]: # 紅色：mid 在最小值左側
                left = mid + 1
            else: # 重複元素
                right -= 1
        return nums[left]
    """
        2b. Binary Search
        如果使用 153. Find Minimum in Rotated Sorted Array 的解法，也就是和最後一個元素比較，
        則可以發現只有前綴和後綴相等的情況下，才會影響一段遞增或兩段遞增的判斷。
        故只要直接去除前綴中和最後一個元素相等的部分，就能直接套用 153 的解法。
        
        但需注意，由於存在重複元素，故藍色的判斷條件需改為 <=
        - 紅：在最小值左側
        - 藍：最小值本身或在最小值右側
    """
    def solve2b(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-2 # [left, right] 由於 nums[n-1] 一定是藍色，所以右界為 n-2
        while (left <= right) and (nums[left] == nums[-1]): # 新增部分：去除前綴中和最後一個元素相等的部分
            left += 1
        while left <= right: # 區間不為空
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]: # 藍色：不管是一段遞增還是兩段遞增，最小值是 mid 或在 mid 的左側，故 mid 不是最小值本身就是在最小值右側
                right = mid - 1
            else: # 紅色：只可能是兩段遞增，最小值一定在 mid 的右側，故 mid 在最小值左側
                left = mid + 1
        return nums[left]