#
# @lc app=leetcode id=2838 lang=python3
# @lcpr version=30204
#
# [2838] Maximum Coins Heroes Can Collect
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        n, m = len(heroes), len(monsters)
        items = sorted(zip(monsters, coins), key=lambda x: x[0])
        s = [0] * (m + 1)
        for i in range(m):
            s[i + 1] = s[i] + items[i][1]
        ans = []
        for hero in heroes:
            ans.append(s[bisect_right(items, hero, key=lambda x: x[0])])
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,4,2]\n[1,1,5,2,3]\n[2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [5]\n[2,3,1,2]\n[10,6,5,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,4]\n[5,7,8]\n[1,1,1]\n
# @lcpr case=end

#

