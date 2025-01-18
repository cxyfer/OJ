# @algorithm @lc id=447 lang=python3 
# @title number-of-boomerangs


from en.Python3.mod.preImport import *
# @test([[0,0],[1,0],[2,0]])=2
# @test([[1,1],[2,2],[3,3]])=2
# @test([[1,1]])=0
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x, y in points: # 枚舉中間的點
            cnt = Counter()
            for x2, y2 in points: # 枚舉兩邊的點
                d = (x - x2) ** 2 + (y - y2) ** 2 # 計算到 (x, y) 的距離，為了消除sqrt的影響，直接取 d^2
                # 確保不會有重複的點，所以 d = 0 的情況不會被計算，不用檢查
                ans += cnt[d] * 2 # 和 (x2, y2) 距離相同的點數量，因為可以交換順序，所以要乘 2
                cnt[d] += 1
        return ans