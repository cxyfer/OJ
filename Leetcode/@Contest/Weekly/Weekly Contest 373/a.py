# You are given a 0-indexed m x n integer matrix mat and an integer k. You have to cyclically right shift odd indexed rows k times and cyclically left shift even indexed rows k times.

# Return true if the initial and final matrix are exactly the same and false otherwise.

from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        if k > n:
            k %= n
        for row in mat:
            if row[-k:] + row[:-k] != row:
                return False
        return True
    
sol = Solution()
print(sol.areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2)) # true
print(sol.areSimilar([[2,2],[2,2]], 3)) # true
print(sol.areSimilar([[1,2]], 1)) # false

print(sol.areSimilar([[4,9,10,10],[9,3,8,4],[2,5,3,8],[6,1,10,4]], 5)) # false