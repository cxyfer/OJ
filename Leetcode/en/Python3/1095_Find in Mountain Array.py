# @algorithm @lc id=1185 lang=python3 
# @title find-in-mountain-array


from en.Python3.mod.preImport import *
class MountainArray:
   def get(self, index: int) -> int:
       ...
   def length(self) -> int:
       ...
# @test([1,2,3,4,5,3,1],3)=2
# @test([0,1,2,4,2,1],3)=-1
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class Solution:
    """
        Binary Search * 3
    """
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # 1. 找到山峰
        left, right = 0, mountain_arr.length() - 1
        peak_idx = 0
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            midl_val = mountain_arr.get(mid - 1)
            midr_val = mountain_arr.get(mid + 1)
            if midl_val < mid_val and mid_val > midr_val: # 找到山峰
                peak_idx = mid
                break
            if midl_val < midr_val: # 山峰在右邊
                left = mid
            else: # 山峰在左邊
                right = mid
        # 2. 在山峰左側(遞增區間)找target
        left, right = 0, peak_idx
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid  # 在左側找到
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        # 3. 在山峰右側(遞減區間)找target
        left, right = peak_idx, mountain_arr.length() - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid  # 在右側找到
            elif mid_val > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1 # 沒找到