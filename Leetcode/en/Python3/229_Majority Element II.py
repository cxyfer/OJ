# @algorithm @lc id=229 lang=python3 
# @title majority-element-ii


from en.Python3.mod.preImport import *
# @test([3,2,3])=[3]
# @test([1])=[1]
# @test([1,2])=[1,2]
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)
        ans = []
        for num in nums:
            cnt[num] += 1
            if cnt[num] == n // 3 + 1:
                ans.append(num)
        return ans