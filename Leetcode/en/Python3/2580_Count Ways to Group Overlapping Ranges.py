# @algorithm @lc id=2651 lang=python3 
# @title count-ways-to-group-overlapping-ranges


from en.Python3.mod.preImport import *
# @test([[6,10],[5,15]])=2
# @test([[1,3],[10,20],[2,5],[4,8]])=4
class Solution:
    """
        區間合併 + 離散數學
    """
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ranges.sort(key=lambda x: x[0]) # 按左端點排序
        cnt, max_r = 0, -float('inf')
        for l, r in ranges:
            if l > max_r: # 若左端點大於前一區間的右端點，則無法合併
                cnt += 1
            max_r = max(max_r, r)
        return pow(2, cnt, MOD)