# @algorithm @lc id=3265 lang=python3 
# @title maximum-good-subarray-sum


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5,6],1)=11
# @test([-1,3,2,4,5],3)=11
# @test([-1,-2,-3,-4],2)=-6
class Solution:
    """
        求 nums[i:j+1] 的和，可以轉換為 prefix sum 的差值，即 s[j] - s[i-1]。
        為滿足 abs(nums[j] - nums[i]) == k ，可以枚舉 j ，考慮 i 的位置，即 nums[i] = nums[j] - k 或 nums[i] = nums[j] + k。
        為使 s[j] - s[i-1] 最大，需要使用Hash表維護最小值維護 s[i-1] 的最小值。 
    """
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -float("inf")
        min_s = defaultdict(lambda: float("inf")) # min prefix sum for s[i-1]
        s = 0 # prefix sum
        for x in nums:
            min_s[x] = min(min_s[x], s) # 維護 s[i-1] 的最小值，需注意不包含 nums[i]
            s += x
            ans = max(ans, s - min_s[x-k], s - min_s[x+k]) # 考慮 nums[i] = nums[j] - k 或 nums[i] = nums[j] + k
        return ans if ans != -float("inf") else 0