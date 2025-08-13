#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 狀態機 DP
令 f[i][j] 表示前 i 個 column 的填法數，且第 i 個 column 的當前狀態為 j 的方案數
- j = 0: 皆為空
- j = 1: 只有上層有塊
- j = 2: 只有下層有塊
- j = 3: 上下層皆有塊

2. 找規律，參考靈神的圖示
f[3] = f[2] + f[1] + 2
f[4] = f[3] + f[2] + (f[1] + 1) * 2
f[5] = f[4] + f[3] + (f[2] + f[1] + 1) * 2
...
f[n-1] = f[n-2] + f[n-3] + (f[n-4] + ... + 1) * 2
f[n] = f[n-1] + f[n-2] + (f[n-3] + f[n-4] + ... + 1) * 2
最後兩式相減得到 f[n] = f[n-1] * 2 + f[n-3]

3. 矩陣快速冪優化
"""
# @lc code=start
class Solution1a:
    def numTilings(self, n: int) -> int:
        MOD = int(1e9 + 7)
        f = [[0] * 4 for _ in range(n + 1)]
        f[1][0] = f[1][3] = 1
        for i in range(2, n + 1):
            f[i][0] = f[i - 1][3]
            f[i][1] = (f[i - 1][0] + f[i - 1][2]) % MOD
            f[i][2] = (f[i - 1][0] + f[i - 1][1]) % MOD
            f[i][3] = (f[i - 1][0] + f[i - 1][1] + f[i - 1][2] + f[i - 1][3]) % MOD
        return f[n][3]

class Solution1b:
    def numTilings(self, n: int) -> int:
        MOD = int(1e9 + 7)
        # 砍掉原本的狀態 0，合併狀態 1 和 2
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = f[1][1] = 1
        for i in range(2, n + 1):
            f[i][0] = 2 * f[i - 2][1] + f[i - 1][0] % MOD
            f[i][1] = (f[i - 2][1] + f[i - 1][0] + f[i - 1][1]) % MOD
        return f[n][1]

class Solution2:
    def numTilings(self, n: int) -> int:
        MOD = int(1e9 + 7)
        f = [0] * (max(n, 2) + 1)
        f[0], f[1], f[2] = 1, 1, 2
        for i in range(3, n + 1):
            f[i] = (f[i-1] * 2 + f[i-3]) % MOD
        return f[n]
    
MOD = int(1e9 + 7)

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        assert len(self.mat[0]) == len(other.mat)
        p, q, r = len(self.mat), len(other.mat), len(other.mat[0])
        res = Matrix([[0] * r for _ in range(p)])
        for k in range(q):
            for i in range(p):
                for j in range(r):
                    res.mat[i][j] += self.mat[i][k] * other.mat[k][j]
                    res.mat[i][j] %= MOD
        return res
    
    def __pow__(self, k):
        assert len(self.mat) == len(self.mat[0])
        n = len(self.mat)
        res = Matrix([[int(i == j) for j in range(n)] for i in range(n)])
        base = self
        while k > 0:
            if k & 1:
                res *= base
            base *= base
            k >>= 1
        return res
    
    def __getitem__(self, i):
        return self.mat[i]
    
class Solution3a:
    def numTilings(self, n: int) -> int:
        if n <= 2: return n
        M = Matrix([[0, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]])
        x = Matrix([[1], [0], [0], [1]])
        res = (M ** (n - 1)) * x
        return res.mat[3][0]
    
class Solution3b:
    def numTilings(self, n: int) -> int:
        if n <= 2: return n
        M = Matrix([[2, 0, 1], [1, 0, 0], [0, 1, 0]])
        x = Matrix([[2], [1], [1]])
        res = (M ** (n - 2)) * x
        return res.mat[0][0]
    
# Solution = Solution1a
Solution = Solution1b
# Solution = Solution2
# Solution = Solution3a
# Solution = Solution3b
# @lc code=end

sol = Solution()
print(sol.numTilings(3))  # 5
print(sol.numTilings(1))  # 1
print(sol.numTilings(4))  # 11