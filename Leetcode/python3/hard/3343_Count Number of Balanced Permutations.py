#
# @lc app=leetcode id=3343 lang=python3
# @lcpr version=30204
#
# [3343] Count Number of Balanced Permutations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = 10**9 + 7
MAXN = 80

fact = [1] * (MAXN + 1)  # fact[i] = i! % MOD
for i in range(1, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD

invf = [1] * (MAXN + 1)  # invf[i] = 1/(i!) % MOD
invf[MAXN] = pow(fact[MAXN], MOD-2, MOD)  # Fermat's little theorem
for i in range(MAXN, 0, -1):
    invf[i-1] = invf[i] * i % MOD

comb = [[0] * (MAXN + 1) for _ in range(MAXN + 1)]  # comb[i][j] = C(i, j) % MOD
for i in range(MAXN + 1):
    comb[i][0] = 1
    for j in range(1, i + 1):
        comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % MOD  # Pascal's triangle

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)

        s = sum(int(ch) for ch in num)
        if s & 1:
            return 0
        n_e, n_o = (n + 1) // 2, n // 2
        cnt = [0] * 10
        for d in num:
            cnt[int(d)] += 1
        @cache
        # d: 當前數字, left_e: 剩餘下標數量, left_s: 剩餘下標和
        def dfs(d, left_e, left_s):
            if d == 10:
                return 1 if left_e == 0 and left_s == 0 else 0
            res = 0
            # 枚舉當前數字 d 選擇的數量 k，則方法數為 comb(cnt[d], k)，並可以遞迴到子問題
            for k in range(0, min(cnt[d], left_e) + 1):
                if k * d > left_s:
                    break
                res = (res + dfs(d + 1, left_e - k, left_s - k * d) * comb[cnt[d]][k]) % MOD
            return res

        ans = dfs(0, n_e, s // 2) * fact[n_e] * fact[n_o] % MOD
        for d in range(10):
            ans = ans * invf[cnt[d]] % MOD
        return ans 
# @lc code=end

sol = Solution()
print(sol.countBalancedPermutations("123")) # 2
print(sol.countBalancedPermutations("112")) # 1
print(sol.countBalancedPermutations("12345")) # 0

#
# @lcpr case=start
# "123"\n
# @lcpr case=end

# @lcpr case=start
# "112"\n
# @lcpr case=end

# @lcpr case=start
# "12345"\n
# @lcpr case=end

#

