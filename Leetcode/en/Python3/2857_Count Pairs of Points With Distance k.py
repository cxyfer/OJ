# @algorithm @lc id=2953 lang=python3 
# @title count-pairs-of-points-with-distance-k


from en.Python3.mod.preImport import *
# @test([[1,2],[4,2],[1,3],[5,2]],5)=2
# @test([[1,3],[1,3],[1,3],[1,3],[1,3]],0)=10
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        """
            1. Brute Force + Hash Table
            (x1 ^ x2) + (y1 ^ y2) = k
            0 <= (x1 ^ x2) <= k
            0 <= (y1 ^ y2) <= k
            x1 ^ x2 = i
            y1 ^ y2 = k - i
            => x1 ^ x2 ^ x2 = i ^ x2 => x1 = i ^ x2
        """
        ans = 0
        cnt = Counter()
        for x1, y1 in coordinates:
            for i in range(k+1):
                ans += cnt[(x1 ^ i, y1 ^ (k - i))]
            cnt[(x1, y1)] += 1
        return ans