# @algorithm @lc id=1657 lang=python3 
# @title find-the-winner-of-an-array-game


from en.Python3.mod.preImport import *
# @test([2,1,3,5,4,6,7],2)=5
# @test([3,2,1],10)=3
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        cur = arr[0]
        win = 0
        for i in range(1, n):
            if arr[i] > cur:
                cur = arr[i]
                win = 0
            win += 1
            if win == k:
                break
        return cur