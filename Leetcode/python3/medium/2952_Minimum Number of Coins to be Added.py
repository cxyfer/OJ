#
# @lc app=leetcode id=2952 lang=python3
# @lcpr version=30203
#
# [2952] Minimum Number of Coins to be Added
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        由小到大構造
        令 s 表示當前可以構造的最大值，則 s+1 為下一個要構造的值
        Time Complexity: O(nlogn + log(target))

        Similar to 1798. Maximum Number of Consecutive Values You Can Make
        Same to 330. Patching Array
    """
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        n = len(coins)
        ans, idx, s = 0, 0, 0
        
        while s < target:
            if idx < n and coins[idx] <= s + 1:
                s += coins[idx] # 可以構造出 [0, s + coins[idx] ] 中的所有整數
                idx += 1
                continue
            else: # 因為後面的硬幣都 > s+1 ，所以無法構造出 s+1 了，需要補充 s+1
                s += s + 1
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,4,10]\n19\n
# @lcpr case=end

# @lcpr case=start
# [1,4,10,5,7,19]\n19\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n20\n
# @lcpr case=end

#

