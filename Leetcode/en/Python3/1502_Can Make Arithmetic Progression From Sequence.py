# @algorithm @lc id=1626 lang=python3 
# @title can-make-arithmetic-progression-from-sequence


from en.Python3.mod.preImport import *
# @test([3,5,1])=true
# @test([1,2,4])=false
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        d = (arr[-1] - arr[0]) // (n-1)
        for i in range(1, n):
            if arr[i] - arr[i-1] != d:
                return False
        return True