# @algorithm @lc id=1925 lang=python3 
# @title count-nice-pairs-in-an-array


from en.Python3.mod.preImport import *
# @test([42,11,1,97])=2
# @test([13,10,35,24,76])=4
class Solution:
    """
        0 <= i < j < nums.length
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        => nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
    """
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        cnt = Counter()
        for x in nums:
            rev_x = int(str(x)[::-1])
            ans += cnt[x - rev_x]
            cnt[x - rev_x] += 1
        return ans % MOD
        