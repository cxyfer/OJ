#
# @lc app=leetcode id=2105 lang=python3
# @lcpr version=30201
#
# [2105] Watering Plants II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        ans = 0
        a, b = capacityA, capacityB
        i, j = 0, n - 1
        while i < j:
            if a < plants[i]: # A 的水不夠，補滿 A 的水
                a = capacityA
                ans += 1
            if b < plants[j]: # B 的水不夠，補滿 B 的水
                b = capacityB
                ans += 1
            a -= plants[i]
            b -= plants[j]
            i += 1
            j -= 1
        if i == j and max(a, b) < plants[i]: # 相遇時水不夠
            ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,2,3,3]\n5\n5\n
# @lcpr case=end

# @lcpr case=start
# [2,2,3,3]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n10\n8\n
# @lcpr case=end

#

