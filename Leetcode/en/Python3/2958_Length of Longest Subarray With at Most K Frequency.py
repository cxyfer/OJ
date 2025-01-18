# @algorithm @lc id=3225 lang=python3 
# @title length-of-longest-subarray-with-at-most-k-frequency


from en.Python3.mod.preImport import *
# @test([1,2,3,1,2,3,1,2],2)=6
# @test([1,2,1,2,1,2,1,2],1)=2
# @test([5,5,5,5,5,5,5],4)=4
class Solution:
    """
        Sliding window
    """
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, num in enumerate(nums): # 枚舉右端點
            cnt[num] += 1
            while cnt[num] > k: # 不符合條件，開始縮小窗口(移動左端點)
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1) # 此時 [left, right] 是符合條件的子陣列，更新答案
        return ans