# @algorithm @lc id=1956 lang=python3 
# @title maximum-element-after-decreasing-and-rearranging


from en.Python3.mod.preImport import *
# @test([2,2,1,2,1])=2
# @test([100,1,1000])=3
# @test([1,2,3,4,5])=5
class Solution:
    """
        Greedy
        滿足題意的array一定是單調遞增的
    """
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        arr[0] = 1
        for i in range(1, n):
            # if arr[i] - arr[i-1] > 1:
            #     arr[i] = arr[i-1] + 1
            arr[i] = min(arr[i], arr[i-1]+1)
        return arr[-1]