# @algorithm @lc id=1392 lang=python3 
# @title find-the-difference-of-two-arrays


from en.Python3.mod.preImport import *
# @test([1,2,3],[2,4,6])=[[1,3],[4,6]]
# @test([1,2,3,3],[1,1,2,2])=[[3],[]]
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res = [[],[]]
        for i in cnt1:
            if i not in cnt2:
                res[0].append(i)
        for i in cnt2:
            if i not in cnt1:
                res[1].append(i)
        return res