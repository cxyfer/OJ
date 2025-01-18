# @algorithm @lc id=3206 lang=python3 
# @title find-common-elements-between-two-arrays


from en.Python3.mod.preImport import *
# @test([4,3,2,3,1],[2,2,5,2,3,6])=[3,4]
# @test([3,4,2,3],[1,5])=[0,0]
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res1 = sum([1 for x in nums1 if x in cnt2])
        res2 = sum([1 for x in nums2 if x in cnt1])
        return [res1, res2]
