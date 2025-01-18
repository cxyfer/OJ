#
# @lc app=leetcode.cn id=2300 lang=python3
#
# [2300] 咒语和药水的成功对数
#
from en.Python3.mod.preImport import *
from bisect import bisect_left
# @lc code=start
class Solution:
    """
        Binary Search
        xy >= success
        => y >= ceil(success/x)
        => y > floor((success-1)/x)
    """
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        potions.sort()
        ans = []
        for x in spells: # 對每個x找到其對應的y，在potions中做一次二分搜尋
            target = (success - 1 ) // x 
            res = bisect_right(potions, target) # bisect_right(> target) ; bisect_left(>= target)
            ans.append(m - res)
        return ans

# @lc code=end

