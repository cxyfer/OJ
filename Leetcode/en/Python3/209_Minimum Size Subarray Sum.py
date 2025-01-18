# @algorithm @lc id=209 lang=python3 
# @title minimum-size-subarray-sum


from en.Python3.mod.preImport import *
# @test(7,[2,3,1,2,4,3])=2
# @test(4,[1,4,4])=1
# @test(11,[1,1,1,1,1,1,1,1])=0
class Solution:
    """
        Sliding window, two pointers (同向雙指標)
        TC: O(n)
        SC: O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        s = 0 # 窗口內數字總和
        left = 0
        for right in range(n): # 枚舉右端點
            s += nums[right]
            while s >= target: # 符合條件，開始縮小窗口(移動左端點)
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0