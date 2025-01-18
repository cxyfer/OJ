# @algorithm @lc id=713 lang=python3 
# @title subarray-product-less-than-k


from en.Python3.mod.preImport import *
# @test([10,5,2,6],100)=8
# @test([1,2,3],0)=0
class Solution:
    """
        # Sliding window, two pointers (同向雙指標)
        Similar to 209. Minimum Size Subarray Sum
    """
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1: # 目標是找乘積小於k的子陣列，如果k=1，則需要乘積<1，但所有數字都>=1，因此也無解
            return 0
        ans = 0
        prod = 1
        left = 0
        for right, x in enumerate(nums): # 枚舉右端點
            prod *= x
            while prod >= k: # 不符合條件，開始縮小窗口(移動左端點)
                prod /= nums[left]
                left += 1
            # 此時 [left, right] 是符合條件的子陣列
            # 在固定右端點的情況下，左端點可以在[left, right]之間任意移動，總共有right-left+1種子陣列
            ans += (right - left + 1)
        return ans