#
# @lc app=leetcode id=3133 lang=python3
# @lcpr version=30204
#
# [3133] Minimum Array End
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
先考慮 x = 0 的情況，不難發現答案就是 n - 1
接著從 x 的二進位表示來考慮，答案就是忽略 x 的二進位表示中 1 的位置，
將 n - 1 填入到 x 的二進位表示中為 0 的位置

1. O(log x + log n)
2. O(log n)
"""
class Solution1:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        i = j = 0
        while n:
            if not x & (1 << i): # x 的第 i 位是 0，可以填充
                if n & (1 << j): # n 的第 j 位是 1，需要填充
                    ans |= (1 << i)
                    n ^= (1 << j)
                j += 1
            i += 1
        return ans

class Solution2:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        t = ~x  # 將 x 取反，用於找到 x 中所有 0 的位置(即取反後的 1 位置)
        while n:
            lb = t & -t # low bit
            if n & 1:
                ans |= lb
            n >>= 1
            t ^= lb # 將 t 中的 lb 位置 1 消除
        return ans
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# 3\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n7\n
# @lcpr case=end

#

