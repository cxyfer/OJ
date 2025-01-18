# @algorithm @lc id=2392 lang=python3 
# @title successful-pairs-of-spells-and-potions


from en.Python3.mod.preImport import *
# @test([5,1,3],[1,2,3,4,5],7)=[4,0,3]
# @test([3,1,2],[8,5,8],16)=[2,0,2]
class Solution:
    """
        Binary Search
        xy >= success
        => y >= ceil(success/x)
        => y >= floor((success-1)/x) + 1
        => y > floor((success-1)/x)
    """
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        ans = []
        for x in spells: # 對每個x找到其對應的y，在potions中做一次二分搜尋
            target = (success - 1) // x
            idx = bisect_right(potions, target) # bisect_right(> target) ; bisect_left(>= target)
            ans.append(m - idx)
        return ans