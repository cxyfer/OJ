#
# @lc app=leetcode id=3335 lang=python3
#
# [3335] Total Characters in String After Transformations I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = int(1e9 + 7)
        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord('a')] += 1

        for _ in range(t):
            nf = [0] * 26
            for i in range(26):
                if i == 25:  # z -> ab
                    nf[0] = (nf[0] + f[i]) % MOD
                    nf[1] = (nf[1] + f[i]) % MOD
                else:
                    nf[i + 1] = (nf[i + 1] + f[i]) % MOD
            f = nf
        return sum(f) % MOD
    
MOD = int(1e9 + 7)
class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        assert len(self.mat[0]) == len(other.mat)
        p, q, r = len(self.mat), len(other.mat), len(other.mat[0])
        res = [[0] * r for _ in range(p)]
        for k in range(q):
            for i in range(p):
                for j in range(r):
                    res[i][j] += self.mat[i][k] * other.mat[k][j]
                    res[i][j] %= MOD
        return Matrix(res)
    
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
    
    def mul_pow(self, k, x):
        assert len(self.mat[0]) == len(x.mat)
        res = x
        while k > 0:
            if k & 1:
                res = self * res
            self = self * self
            k >>= 1
        return res
    
    def __getitem__(self, i):
        return self.mat[i]

    def __str__(self):
        return "\n".join(map(lambda x: " ".join(map(str, x)), self.mat))

class Solution2:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        M = Matrix([[0] * 26 for _ in range(26)])
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                M[i][j] = 1
        x = Matrix([[1] for _ in range(26)])
        M = M.mul_pow(t, x)
        ans = 0
        for i in range(26):
            ans += cnt[i] * M[i][0]
            ans %= MOD
        return ans
    
Solution = Solution1
# Solution = Solution2
# @lc code=end

