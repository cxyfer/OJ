#
# @lc app=leetcode id=2965 lang=python3
# @lcpr version=30203
#
# [2965] Find Missing and Repeated Values
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    1. Hash Table
    2. Bit Manipulation
        - Similar to 260. Single Number III
    3. Math
"""
# @lc code=start
class Solution1:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = [0] * (n * n + 1)
        for row in grid:
            for x in row:
                cnt[x] += 1
        ans = [-1, -1]
        for i in range(1, n * n + 1):
            if cnt[i] == 2: # repeated, a
                ans[0] = i
            elif cnt[i] == 0: # missing, b
                ans[1] = i
        return ans
    
class Solution2:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        _xor = reduce(xor, (x for row in grid for x in row))
        _xor ^= reduce(xor, (x for x in range(1, n * n + 1)))
        # 分組異或
        lb = _xor & -_xor # 最低位的 1
        ans = [0, 0]
        for row in grid:
            for x in row:
                ans[x & lb == 0] ^= x # 分組異或
        for x in range(1, n * n + 1):
            ans[x & lb == 0] ^= x # 分組異或
        return ans if ans[0] in [x for row in grid for x in row] else ans[::-1]
    
class Solution3:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid) ** 2
        s1 = sum(x for row in grid for x in row) # sum of all numbers
        s2 = sum(x * x for row in grid for x in row) # sum of all squares
        d1 = s1 - m * (m + 1) // 2 # a - b
        d2 = s2 - m * (m + 1) * (m * 2 + 1) // 6 # a^2 - b^2 = (a + b)(a - b)
        return [(d2 // d1 + d1) // 2, (d2 // d1 - d1) // 2] # (a, b)
    
# class Solution(Solution1):
# class Solution(Solution2):
class Solution(Solution3):
    pass
# @lc code=end

sol = Solution()
print(sol.findMissingAndRepeatedValues([[1,3],[2,2]])) # [2, 4]
print(sol.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])) # [9, 5]

#
# @lcpr case=start
# [[1,3],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[9,1,7],[8,9,2],[3,4,6]]\n
# @lcpr case=end

#

