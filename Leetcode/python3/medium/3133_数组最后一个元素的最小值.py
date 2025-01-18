#
# @lc app=leetcode.cn id=3133 lang=python3
#
# [3133] 数组最后一个元素的最小值
#

# @lc code=start
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # return self.solve1(n, x)
        return self.solve2(n, x)
    """
        1. O(log x + log n)
    """
    def solve1(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        i = j = 0
        while n:
            if not x & (1 << i): # x 的第 i 位是 0，可以填充
                if n & (1 << j): # n 的第 j 位是 1，需要填充
                    ans |= (1 << i)
                    n -= (1 << j)
                j += 1
            i += 1
        return ans
    """
        2. O(log n)
    """
    def solve2(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        t = ~x # x 取反，用於找到 x 中所有 0 的位置(取反後的 1 位置)
        j = 0
        while n >> j:
            lb = t & -t
            if (n >> j) & 1:
                ans |= lb
            j += 1
            t ^= lb # 將 t 中的 lb 位置 1 消除
        return ans
# @lc code=end

