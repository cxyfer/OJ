#
# @lc app=leetcode id=600 lang=python3
# @lcpr version=30204
#
# [600] Non-negative Integers without Consecutive Ones
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
Digit DP
這裡是轉換為二進位制字串後，再由最高位(下標為0)開始

Reference:
- https://algo.itcharge.cn/10.Dynamic-Programming/09.Digit-DP/01.Digit-DP/
- https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/solutions/1750941/by-endlesscheng-1egu/?envType=daily-question&envId=2024-08-05
"""
class Solution1:
    def findIntegers(self, n: int) -> int:
        s = format(n, 'b') # to binary string
        @cache # memoization
        def dfs(i: int, pre: bool, is_limit: bool) -> int:
            """
                i: current index
                pre: is previous digit is 0
                is_limit: is bounded to maximum value n
            """
            if i == len(s): # 填完所有位數
                return 1
            up = int(s[i]) if is_limit else 1 # 當前可以填的數字上界
            res = dfs(i + 1, False, is_limit and up == 0) # 當前位數填0
            if not pre and up == 1: # 若前一位是0，且當前位可以填入1
                res += dfs(i + 1, True, is_limit and up == 1) # 當前位數填1
            return res
        return dfs(0, False, True)
    
class Solution2:
    def findIntegers(self, n: int) -> int:
        @cache # memoization
        def dfs(i: int, pre: bool, is_limit: bool) -> int:
            if i < 0: # 填完所有位數
                return 1
            up = (n >> i) & 1 if is_limit else 1 # 當前可以填的數字上界
            res = dfs(i - 1, False, is_limit and up == 0) # 當前位數填0
            if not pre and up == 1: # 若前一位是0，且當前位可以填入1
                # res += dfs(i - 1, True, is_limit and up == 1) # 當前位數填1
                res += dfs(i - 1, True, is_limit) # 當前位數填1
            return res
        return dfs(n.bit_length() - 1, False, True)
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.findIntegers(5))
print(sol.findIntegers(1))
print(sol.findIntegers(2))

#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

