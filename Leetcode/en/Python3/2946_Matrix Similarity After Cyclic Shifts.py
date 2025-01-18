# @algorithm @lc id=3215 lang=python3 
# @title matrix-similarity-after-cyclic-shifts


from en.Python3.mod.preImport import *
# @test([[1,2,1,2],[5,5,5,5],[6,3,6,3]],2)=true
# @test([[2,2],[2,2]],3)=true
# @test([[1,2]],1)=false
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        if k > n:
            k %= n
        for row in mat:
            if row[-k:] + row[:-k] != row:
                return False
        return True