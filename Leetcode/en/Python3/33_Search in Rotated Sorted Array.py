# @algorithm @lc id=33 lang=python3 
# @title search-in-rotated-sorted-array


from en.Python3.mod.preImport import *
# @test([4,5,6,7,0,1,2],0)=4
# @test([4,5,6,7,0,1,2],3)=-1
# @test([1],0)=-1
class Solution:
    """
        1. 兩次二分查找
        2. 一次二分查找
    """
    def search(self, nums: List[int], target: int) -> int:
        # return self.solve1(nums, target)
        return self.solve2(nums, target)
    """
        1. 兩次二分查找
        基於 153. Find Minimum in Rotated Sorted Array 找到最小值的位置，
        再根據 target 和 nums[-1] 的大小關係，確定 target 在左段還是右段，再進行二分查找
    """
    def solve1(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int: # 153. Find Minimum in Rotated Sorted Array
            n = len(nums)
            left, right = 0, n-2 # [left, right] 由於 nums[n-1] 一定是藍色，所以右界為 n-2
            while left <= right: # 區間不為空
                mid = (left + right) // 2
                if nums[mid] < nums[-1]: # 藍色：不管是一段遞增還是兩段遞增，最小值是 mid 或在 mid 的左側，故 mid 不是最小值本身就是在最小值右側
                    right = mid - 1
                else: # 紅色：只可能是兩段遞增，最小值一定在 mid 的右側，故 mid 在最小值左側
                    left = mid + 1
            return left # or right+1
        n = len(nums)
        i = findMin(nums) # min index
        if target > nums[-1]: # target 在左段
            left, right = 0, i-1 # [left, right]
        else: # target 在右段
            left, right = i, n - 1 # [left, right]
        idx = bisect_left(nums, target, left, right+1) # [lo, hi)
        return idx if idx < n and nums[idx] == target else -1
    """
        2. 一次二分查找
        分類討論：
        可以根據 nums[i] 和 nums[-1] 的大小關係，確定當前位置 i 在左段還是右段，同理可應用於 target
        再根據這些點的位置關係，可以決定 target 是不是在 nums[i] 的左側 (要不要將nums[i] 染成藍色)

        紅色：target左側
        藍色：target及其右側
    """
    def solve2(self, nums: List[int], target: int) -> int:
        def check(i: int) -> bool: # 檢查 nums[i] 是否為target或其右側 (藍色)
            if nums[i] > nums[-1]: # 兩段遞增，且nums[i] 在左段
                return target > nums[-1] and nums[i] >= target # target 也在左段，且在 nums[i] 的左側 (或是 nums[i] 本身)
            else: # nums[i] 在 兩段遞增的右段 或 只有一段遞增
                return target > nums[-1] or nums[i] >= target # target 在兩段遞增的左段、或在 nums[i] 的左側 (或是 nums[i] 本身)
        n = len(nums)
        left, right = 0, n-1 # [left, right]
        while left <= right: # 區間不為空
            mid = (left + right) // 2
            if check(mid): # 藍色
                right = mid - 1
            else: # 紅色
                left = mid + 1
        return left if nums[left] == target else -1