# @algorithm @lc id=1776 lang=python3 
# @title minimum-operations-to-reduce-x-to-zero


from en.Python3.mod.preImport import *
# @test([1,1,4,2,3],5)=2
# @test([5,6,7,8,9],4)=-1
# @test([3,2,20,1,1,3],10)=5
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # return self.solve1(nums, x)
        return self.solve2(nums, x)
    """
        1. Two pointers
    """
    def solve1(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        pre_sum, suf_sum = 0, 0 # prefix sum, suffix sum
        while left < n and pre_sum < x:
            pre_sum += nums[left]
            left += 1
        if left == n and pre_sum < x:
            return -1
        ans = left if pre_sum == x else float("inf")

        while left <= right and left > 0 and right >= 0:
            pre_sum -= nums[left-1] # 左邊少取一個
            left -= 1
            while pre_sum + suf_sum < x and right >= 0: # 右邊取到剩餘的和>=x
                suf_sum += nums[right]
                right -= 1
            if pre_sum + suf_sum == x:
                ans = min(ans, left + n - 1 - right)
        return ans if ans != float('inf') else -1
    """
        2. Sliding window
        將問題轉換成取一段連續的子數組和等於sum(nums) - x
    """
    def solve2(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target == 0:
            return n
        if target < 0:
            return -1
        left = 0
        cur_sum = 0
        ans = -1
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum > target and left <= right: # 縮小窗口
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                ans = max(ans, right - left + 1)
        return n - ans if ans != -1 else -1