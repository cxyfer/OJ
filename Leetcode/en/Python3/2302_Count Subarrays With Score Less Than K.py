# @algorithm @lc id=2394 lang=python3 
# @title count-subarrays-with-score-less-than-k


from en.Python3.mod.preImport import *
# @test([2,1,4,3,5],10)=6
# @test([1,1,1],5)=5
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        s = 0
        for right in range(n): # 枚舉右端點
            s += nums[right]
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1 # 以 right 為右端點，且滿足條件的子陣列數量
        return ans