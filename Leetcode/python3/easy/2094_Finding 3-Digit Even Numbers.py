#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Enumeration
2. Backtracking
"""
# @lc code=start
class Solution1:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        ans = []
        for i in range(100, 1000, 2):
            if Counter(map(int, str(i))) <= cnt:
                ans.append(i)
        return ans
    
class Solution2:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        ans = []
        def dfs(i, x):
            if i == 3:
                if x % 2 == 0:
                    ans.append(x)
                return
            for j in range(10):
                if i == 0 and j == 0 or cnt[j] <= 0:
                    continue
                cnt[j] -= 1
                dfs(i + 1, x * 10 + j)
                cnt[j] += 1
        dfs(0, 0)
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

