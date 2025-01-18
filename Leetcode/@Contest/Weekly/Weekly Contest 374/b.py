# You are given a 0-indexed integer array coins, representing the values of the coins available, and an integer target.

# An integer x is obtainable if there exists a subsequence of coins that sums to x.

# Return the minimum number of coins of any value that need to be added to the array so that every integer in the range [1, target] is obtainable.

# A subsequence of an array is a new non-empty array that is formed from the original array by deleting some (possibly none) of the elements without disturbing the relative positions of the remaining elements.

from typing import List

class Solution:
    """
        由小到大構造
        令 s 表示當前可以構造的最大值，則 s+1 為下一個要構造的值
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

sol = Solution()
print(sol.minimumAddedCoins([1,4,10], 19)) # 2
print(sol.minimumAddedCoins([1,4,10,5,7,19], 19)) # 1
print(sol.minimumAddedCoins([1,1,1], 20)) # 3
print(sol.minimumAddedCoins([100000], 100000)) # 17