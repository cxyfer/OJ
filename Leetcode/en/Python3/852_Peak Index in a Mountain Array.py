# @algorithm @lc id=882 lang=python3 
# @title peak-index-in-a-mountain-array


from en.Python3.mod.preImport import *
# @test([0,1,0])=1
# @test([0,2,1,0])=1
# @test([0,10,5,2])=1
class Solution:
    """
        Binary Search
        Time: O(logn)
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1
        while left <= right: # [left, right]
            mid = (left + right) // 2
            if arr[mid] > arr[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        return left