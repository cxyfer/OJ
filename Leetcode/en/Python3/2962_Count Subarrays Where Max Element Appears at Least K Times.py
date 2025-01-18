# @algorithm @lc id=3213 lang=python3 
# @title count-subarrays-where-max-element-appears-at-least-k-times


from en.Python3.mod.preImport import *
# @test([1,3,2,3,3],2)=6
# @test([1,4,2,1],3)=0
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        return self.solve1(nums, k)
        # return self.solve2(nums, k)
    """
        1. Sliding window
    """
    def solve1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)
        cnt = 0 # count of mx
        left = 0
        ans = 0
        for right in range(n):
            if nums[right] == mx:
                cnt += 1
            while cnt == k: # 讓窗口保持在 left -= 1 就能滿足 cnt == k 的狀態
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ans += left
        return ans
    """
        2. Prefix sum + Binary search
    """
    def solve2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)

        pre = [0]
        for num in nums:
            pre.append(pre[-1] + (num == mx))
        ans = 0

        for i in range(n): # 對於每個 i，找到 pre[i] + k 的位置
            j = bisect_left(pre, pre[i] + k)
            ans += n - (j - 1)
        return ans