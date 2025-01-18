# @algorithm @lc id=1463 lang=python3 
# @title the-k-weakest-rows-in-a-matrix


from en.Python3.mod.preImport import *
# @test([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3)=[2,0,3]
# @test([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],2)=[0,2]
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