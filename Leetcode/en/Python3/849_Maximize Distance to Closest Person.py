# @algorithm @lc id=879 lang=python3 
# @title maximize-distance-to-closest-person


from en.Python3.mod.preImport import *
# @test([1,0,0,0,1,0,1])=2
# @test([1,0,0,0])=3
# @test([0,1])=1
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        ans = 0
        l = 0
        for idx in range(n):
            if seats[idx] == 1:
                if l == 0 and seats[0] == 0: # if leftmost seat is empty
                    ans = idx
                ans = max(ans, (idx-l)//2) # middle seat
                l = idx # Updata left seat index
        if seats[n-1] == 0:
            ans = max(ans, n - 1 - l ) # if rightmost seat is empty
        return ans