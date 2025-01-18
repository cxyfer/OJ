# @algorithm @lc id=2047 lang=python3 
# @title find-a-peak-element-ii


from en.Python3.mod.preImport import *
# @test([[1,4],[3,2]])=[0,1]
# @test([[10,20,15],[21,30,14],[7,16,32]])=[1,1]
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # return self.solve1(mat)
        return self.solve2(mat)
    """
        1. Brute Force
        遍歷所有元素，找到最大值
    """
    def solve1(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = [0, 0]
        for i in range(m):
            for j in range(n):
                if mat[i][j] > mat[ans[0]][ans[1]]:
                    ans = [i, j]
        return ans
    """
        2. Binary Search
    """
    def solve2(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, m - 2
        while left <= right:
            mid = (left + right) // 2
            mx, idx = max((v, i) for i, v in enumerate(mat[mid]))
            if mx > mat[mid + 1][idx]: # 峰頂在這row或在上半部分，row_idx <= i
                right = mid - 1 
            else: # 峰頂在下半部分，row_idx > i
                left = mid + 1
        i = left
        _, j = max((v, j) for j, v in enumerate(mat[i]))
        return [i, j]