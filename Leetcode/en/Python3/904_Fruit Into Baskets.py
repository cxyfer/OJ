# @algorithm @lc id=940 lang=python3 
# @title fruit-into-baskets


from en.Python3.mod.preImport import *
from collections import Counter
# @test([1,2,1])=3
# @test([0,1,2,2])=3
# @test([1,2,3,2,2])=4
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Sliding window, two pointers
        # Similar to 209. Minimum Size Subarray Sum
        ans = 0
        sum = 0 # 裝的水果種類數量，最多只能裝2種
        cnt = Counter()
        left = 0
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            if cnt[fruit] == 1: # cnt[fruit] 從0變成1，代表有新的水果種類
                sum += 1 
            while sum > 2: # 超過2種水果，縮小窗口
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0: # cnt[fruits[left]] 從1變成0，代表水果種類減少
                    sum -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans