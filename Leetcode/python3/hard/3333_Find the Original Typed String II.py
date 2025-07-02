#
# @lc app=leetcode id=3333 lang=python3
#
# [3333] Find the Original Typed String II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:
            return 0
        groups = [len(list(g)) for _, g in groupby(word)]
        m = len(groups)
        need = k - m  # 每組至少要選 1 個，剩下 k - m 個要選
        tot = reduce(lambda x, y: (x * y) % MOD, groups)
        if need <= 0:
            return tot
        
        # 長度至少為 k 的方案數 = 總方案數 - 長度不超過 k 的方案數
        f = [0] * (need)  # 長度不超過 k 的方案數 = 長度最多為 k - 1 的方案數
        f[0] = 1
        for ln in groups:
            if ln - 1 <= 0:
                continue
            # 前綴和優化 DP
            s = list(accumulate(f, lambda x, y: (x + y) % MOD, initial=0))
            for i in range(need):
                f[i] = (s[i + 1] - s[max(0, i - (ln - 1))]) % MOD
        return (tot - reduce(lambda x, y: (x + y) % MOD, f)) % MOD
# @lc code=end

