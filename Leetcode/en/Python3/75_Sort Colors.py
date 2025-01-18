# @algorithm @lc id=75 lang=python3 
# @title sort-colors


from en.Python3.mod.preImport import *
# @test([2,0,2,1,1,0])=[0,0,1,1,2,2]
# @test([2,0,1])=[0,1,2]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.sovleBySort(nums) # O(nlogn)
        self.solveByTwoPointer(nums) # O(n)

    def sovleBySort(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            swap(i, min_idx)
        return
    """
        Two Pointer
        把 0 放到前面，2 放到後面，1 就會在中間
    """
    def solveByTwoPointer(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return
        l, r, idx = 0, n-1, 0
        while idx <= r:
            if nums[idx] == 0: # 把 0 放到前面
                nums[l], nums[idx] = nums[idx], nums[l]
                l += 1
                idx += 1
            elif nums[idx] == 2: # 把 2 放到後面
                nums[r], nums[idx] = nums[idx], nums[r]
                r -= 1
            else:
                idx += 1
        return
