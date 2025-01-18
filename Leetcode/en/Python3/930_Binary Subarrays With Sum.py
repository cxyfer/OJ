# @algorithm @lc id=966 lang=python3 
# @title binary-subarrays-with-sum


from en.Python3.mod.preImport import *
# @test([1,0,1,0,1],2)=4
# @test([0,0,0,0,0],0)=15
class Solution:
    """
        Prefix sum + Hash Table
    """
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = defaultdict(int)
        s = 0 # prefix sum
        ans = 0
        for x in nums:
            cnt[s] += 1
            s += x 
            ans += cnt[s - goal]
        return ans