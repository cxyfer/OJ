# @algorithm @lc id=2665 lang=python3 
# @title minimum-time-to-repair-cars


from en.Python3.mod.preImport import *
# @test([4,2,3,1],10)=16
# @test([5,1,8],6)=16
class Solution:
    """
        Binary Search
    """
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0 # 下界
        right = min(ranks) * cars * cars # 上界
        while left < right - 1:
            mid = (left + right) // 2
            if sum(int(math.sqrt(mid // r)) for r in ranks) >= cars:
                right = mid
            else:
                left = mid
        return right