#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Sliding window
1a. Hash table
1b. Array
"""
# @lc code=start
class Solution1a:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = defaultdict(int)
        ans = left = 0
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    
class Solution1b:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = [0] * (len(fruits) + 1)
        ans = left = tot = 0
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            if cnt[fruit] == 1:
                tot += 1
            while tot > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    tot -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    
# Solution = Solution1a
Solution = Solution1b
# @lc code=end
# @lc code=end