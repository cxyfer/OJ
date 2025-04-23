#
# @lc app=leetcode id=2338 lang=python3
#
# [2338] Count the Number of Ideal Arrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
MAX_N = int(1e4)
MAX_E = math.ceil(math.log2(MAX_N))

# 預處理 Least Prime Factor (LPF)
LPF = [0] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    if LPF[i] == 0:  # i is prime
        LPF[i] = i
        for j in range(i * i, MAX_N + 1, i):
            if LPF[j] == 0:
                LPF[j] = i

# 質因數分解
EXP = [defaultdict(int) for _ in range(MAX_N + 1)]
for x in range(2, MAX_N + 1):
    t = x
    while t > 1:
        p = LPF[t]
        EXP[x][p] += 1
        t //= p

# 預處理 comb
COMB = [[0] * (MAX_E + 1) for _ in range(MAX_N + MAX_E)]
for i in range(MAX_N + MAX_E):
    COMB[i][0] = 1
    for j in range(1, min(i, MAX_E) + 1):
        COMB[i][j] = (COMB[i - 1][j] + COMB[i - 1][j - 1]) % MOD

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for x in range(1, maxValue + 1):  # 枚舉最大值
            cur = 1
            for e in EXP[x].values():
                cur = cur * COMB[n + e - 1][e] % MOD
            ans = (ans + cur) % MOD
        return ans
# @lc code=end

sol = Solution()
print(sol.idealArrays(2, 5))  # 10