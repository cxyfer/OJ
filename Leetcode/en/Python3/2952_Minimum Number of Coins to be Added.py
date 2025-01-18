# @algorithm @lc id=3231 lang=python3 
# @title minimum-number-of-coins-to-be-added


from en.Python3.mod.preImport import *
# @test([1,4,10],19)=2
# @test([1,4,10,5,7,19],19)=1
# @test([1,1,1],20)=3
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