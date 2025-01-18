# @algorithm @lc id=1121 lang=python3 
# @title partition-array-for-maximum-sum


from en.Python3.mod.preImport import *
# @test([1,15,7,9,2,5,10],3)=84
# @test([1,4,1,5,7,3,6,1,9,9,3],4)=83
# @test([1],1)=1
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        @cache
        def dfs(i: int) -> int:
            res = 0 # result
            mx = 0 # max value in the current window
            for j in range(i, min(i + k, n)):
                mx = max(mx, arr[j]) # update max value of the current window
                res = max(res, mx * (j - i + 1) + dfs(j + 1)) # update result
            return res
        
        return dfs(0)