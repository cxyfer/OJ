#
# @lc app=leetcode id=3699 lang=python3
#
# [3699] Number of ZigZag Arrays I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
import numpy as np

MOD = int(1e9) + 7


class Solution1:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f0 = [1] * V
        f1 = [1] * V
        for _ in range(1, n):
            # 這裡加上 func=lambda x, y: (x + y) % MOD 反而會 TLE
            s0 = list(accumulate(f0, initial=0))
            s1 = list(accumulate(f1, initial=0))
            for curr in range(V):
                # 可以用 prefix sum 來優化以下這個被註解掉的迴圈
                # 且因為 f 被保存在 s 中了，所以直接覆蓋 f 就好
                # for prev in range(V):
                #     nf0[curr] += f1[prev] if curr < prev else 0
                #     nf1[curr] += f0[prev] if curr > prev else 0
                f0[curr] = s1[curr] % MOD
                f1[curr] = (s0[V] - s0[curr + 1]) % MOD
        print(f0, f1)
        return (sum(f0) + sum(f1)) % MOD


class Solution2:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f = [1] * V
        for i in range(1, n):
            # 由於 ZigZag 是有對稱性的，因此只需要算 f0 或 f1 的其中一個即可，最後再乘以 2
            # 而上述轉移其實就是把 f0 更新為 f1 的 prefix sum，f1 更新為 f0 的 suffix sum，兩者交替
            # 因此可以只保留 f0，並根據 i 的奇偶性來決定是算 prefix sum 還是 suffix sum
            if i & 1:
                f = list(accumulate(f, initial=0))[:-1]
            else:
                f = list(accumulate(f[::-1], initial=0))[:-1][::-1]
            f = [v % MOD for v in f]
        return sum(f) * 2 % MOD


class Solution2np:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f = np.ones(V, dtype=np.int64)
        for i in range(1, n):
            if i & 1:
                f[1:] = np.cumsum(f[:-1])
                f[0] = 0
            else:
                f[:-1] = np.cumsum(f[:0:-1])[::-1]
                f[-1] = 0
            f = f % MOD
        return int(np.sum(f) * 2 % MOD)


class Solution3:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f = [1] * V
        for _ in range(1, n):
            # 把 i & 1 的情況中計算後綴前需要的翻轉，移動到 i & 1 == 0 中計算完成後
            # 這樣可以把兩種情況寫成同一個式子
            f = list(accumulate(f, initial=0))[:-1][::-1]
            f = [v % MOD for v in f]
        return sum(f) * 2 % MOD


class Solution3np:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        V = r - l + 1  # [l, r] => [0, V - 1]
        f = np.ones(V, dtype=np.int64)
        for _ in range(1, n):
            f[1:] = np.cumsum(f[:-1])
            f[0] = 0
            f = f[::-1] % MOD
        return int(np.sum(f)) * 2 % MOD


Solution = Solution1
# Solution = Solution2
# Solution = Solution2np
# Solution = Solution3
# Solution = Solution3np
# @lc code=end

sol = Solution()
print(sol.zigZagArrays(3, 4, 5))  # 2
print(sol.zigZagArrays(3, 1, 3))  # 10
# print(sol.zigZagArrays(7, 9, 39))  # 650716800
# print(sol.zigZagArrays(30, 7, 809))  # 505683848
# print(sol.zigZagArrays(2000, 347, 1391))  # 186018700