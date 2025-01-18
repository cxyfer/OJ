# @algorithm @lc id=2428 lang=python3 
# @title equal-row-and-column-pairs


from en.Python3.mod.preImport import *
# @test([[3,2,1],[1,7,6],[2,7,7]])=1
# @test([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])=3
class Solution:
    """
        Hash Map
        1. 對於每一列，計算其出現次數
        2. 再對於每一行檢查是否與某一列相等，若相等則加上該列出現次數
    """
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = Counter([tuple(row) for row in grid])
        return sum(cnt[col] for col in zip(*grid))