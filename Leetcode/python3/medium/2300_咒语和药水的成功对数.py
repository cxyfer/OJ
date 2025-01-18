#
# @lc app=leetcode.cn id=2300 lang=python3
# @lcpr version=30108
#
# [2300] 咒语和药水的成功对数
#
from preImport import *
# @lc code=start
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
# @lc code=end



#
# @lcpr case=start
# [5,1,3]\n[1,2,3,4,5]\n7\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2]\n[8,5,8]\n16\n
# @lcpr case=end

#

