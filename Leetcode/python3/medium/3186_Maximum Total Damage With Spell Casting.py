#
# @lc app=leetcode id=3186 lang=python3
# @lcpr version=30203
#
# [3186] Maximum Total Damage With Spell Casting
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

class Solution1:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        keys = sorted(cnt.keys())
        m = len(keys)

        dp = [0] * m
        dp[0] = keys[0] * cnt[keys[0]]
        mx = [dp[0]] + [0] * m # mx[i] = max(dp[0], dp[1], ..., dp[i])
        for i in range(1, m):
            for j in range(i-1, -1, -1): # 每次最多看 3 個數
                d = keys[i] - keys[j]
                if d <= 2:
                    continue
                # dp[i] = max(dp[i], dp[j]) # 可以維護 mx ，這樣就能用下面兩行取代
                dp[i] = max(dp[i], mx[j])
                break
            dp[i] += keys[i] * cnt[keys[i]]
            mx[i] = max(mx[i - 1], dp[i])
        return max(dp)
    
class Solution2a:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        keys = sorted(cnt.keys())
        m = len(keys)

        @cache
        def dfs(i: int) -> int: # 考慮到第 i 個數字時的最大總傷害
            if i < 0:
                return 0
            j = i - 1
            while j >= 0 and keys[i] - keys[j] <= 2:
                j -= 1
            return max(dfs(i - 1), dfs(j) + keys[i] * cnt[keys[i]])
        
        return dfs(m - 1)
    
class Solution2b:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        keys = sorted(cnt.keys())
        m = len(keys)

        dp = [0] * (m + 1)
        j = 0 # 上一個可選的數字的下標
        for i, x in enumerate(keys, start=1):
            while keys[j] < x - 2:
                j += 1
            dp[i] = max(dp[i - 1], dp[j] + x * cnt[x])

        return dp[-1]

class Solution(Solution1):
    pass

# class Solution(Solution2a):
#     pass

# class Solution(Solution2b):
#     pass
# @lc code=end

sol = Solution()
print(sol.maximumTotalDamage([1,1,3,4])) # 6
print(sol.maximumTotalDamage([7,1,6,6])) # 13
print(sol.maximumTotalDamage([7,1,6,3])) # 10
print(sol.maximumTotalDamage([5,9,2,10,2,7,10,9,3,8])) # 31

#
# @lcpr case=start
# [1,1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,1,6,6]\n
# @lcpr case=end

#

