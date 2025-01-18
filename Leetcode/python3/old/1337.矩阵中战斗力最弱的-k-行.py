#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Binary Search + Heap
    """
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # return [idx for idx, _ in sorted([(idx, sum(row)) for idx, row in enumerate(mat)], key=lambda x:x[1])[:k]]
        m, n = len(mat), len(mat[0])
        heap = []
        for idx, row in enumerate(mat):
            cnt = n - bisect_left(row[::-1], 1) # 計算1的個數
            heapq.heappush(heap, (-cnt, -idx))
            if len(heap) > k:
                heapq.heappop(heap)
        heap.sort(reverse=True)
        return [-idx for _, idx in heap]

# @lc code=end
sol = Solution()
print(sol.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))
