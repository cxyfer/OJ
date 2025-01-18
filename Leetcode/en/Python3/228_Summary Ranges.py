# @algorithm @lc id=228 lang=python3 
# @title summary-ranges


from en.Python3.mod.preImport import *
# @test([0,1,2,4,5,7])=["0->2","4->5","7"]
# @test([0,2,3,4,6,8,9])=["0","2->4","6","8->9"]
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Two pointers
        n = len(nums)
        left = 0
        ans = []
        for right in range(1, n+1): 
            if right < n and nums[right] == nums[right-1] + 1:
                continue
            if left == right-1:
                ans.append(str(nums[left]))
            else:
                ans.append(f"{nums[left]}->{nums[right-1]}")
            left = right
        return ans