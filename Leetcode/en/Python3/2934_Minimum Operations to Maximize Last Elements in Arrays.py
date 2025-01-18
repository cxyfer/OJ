# @algorithm @lc id=3190 lang=python3 
# @title minimum-operations-to-maximize-last-elements-in-arrays


from en.Python3.mod.preImport import *
# @test([1,2,7],[4,5,3])=1
# @test([2,3,4,5,9],[8,8,4,4,4])=2
# @test([1,5,4],[2,5,3])=-1
class Solution:
    """
        考慮兩種情況
        1. 換了最後一組
        2. 沒換最後一組
    """
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        def f(last1, last2):
            res = 0
            for x, y in zip(nums1, nums2):
                if x > last1 or y > last2:
                    if y > last1 or x > last2: # 不能換
                        return float('inf')
                    res += 1 # 可以換
            return res
        res1 = f(nums1[-1], nums2[-1])
        res2 = f(nums2[-1], nums1[-1])
        return min(res1, res2) if min(res1, res2) != float('inf') else -1