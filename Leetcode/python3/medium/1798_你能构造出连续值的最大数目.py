1#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#
from typing import List
# @lc code=start
class Solution:
    """
        由小到大構造
        令 s 表示當前可以構造的最大值，則 s+1 為下一個要構造的值
        Similar to 330. Patching Array
        Similar to 2952. Minimum Number of Coins to be Added
    """
class Solution:
    """
        由小到大構造
        令 s 表示當前可以構造的最大值，則 s+1 為下一個要構造的值
        Similar to 330. Patching Array
        Similar to 2952. Minimum Number of Coins to be Added
    """
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        s = 0 # 可以構造的最大值
        
        for c in coins:
            if c <= s + 1:
                s += c # 可以構造出 [0, s+c] 中的所有整數
            else: # 因為後面的硬幣都 > s+1 ，所以無法構造出 s+1 了
                break

        return s + 1 # [0, s] 之間有 s+1 個整數
# @lc code=end

