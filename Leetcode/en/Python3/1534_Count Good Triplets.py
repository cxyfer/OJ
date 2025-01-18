# @algorithm @lc id=1656 lang=python3 
# @title count-good-triplets


from en.Python3.mod.preImport import *
# @test([3,0,1,1,9,7],7,2,3)=4
# @test([1,1,2,2,3],0,0,1)=0
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if abs(arr[i]-arr[j]) > a:
                    continue
                for k in range(j+1, n):
                    # if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                    if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        ans += 1
        return ans