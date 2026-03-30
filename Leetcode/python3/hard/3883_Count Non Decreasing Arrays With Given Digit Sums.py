#
# @lc app=leetcode id=3883 lang=python3
#
# [3883] Count Non Decreasing Arrays With Given Digit Sums
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
## 1. 前綴和優化DP

預先處理 [0, 5000] 內數字的 digit sum，並將數字按照 digit sum 分組。
令 groups[d] 表示 digit sum 為 d 的數字列表。

令 f[i][v] 表示考慮到第 i 個數字，且，最後一個數字為 v 時的合法陣列數量。
而當前位置的 digitSum[i] 為 d 時，則可以填入 groups[d] 中的數字。
對於 groups[d] 中的每個數字 x，只要 v <= x，則有 f[i][x] += f[i - 1][v] 的轉移。

但這樣的轉移對於每個數字都要遍歷一次 f 的值域，太慢了。
注意到我們轉移時只需要取 f 的前綴區間和，因此可以對 f 做前綴和來優化轉移過程。

## 2. 雙指標優化DP
從方法一中注意到我們實際上不用更新 f 的所有位置，只需要更新 groups[cur] 中的數字即可。
因此我們實際上只需要計算 groups[pre] 中 <= x 的數字的 f 值之和。
而我們在枚舉時，可以確保 x 的大小順序，而轉移的來源也能確保大小順序。
因此可以利用雙指標來優化轉移過程。
"""

MOD = int(1e9 + 7)

MAX_V = int(5e3)
MAX_S = 50
digitSum = [0] * (MAX_V + 1)
groups = [[] for _ in range(MAX_S + 1)]
for x in range(MAX_V + 1):
    # s = sum(int(d) for d in str(x))
    s = digitSum[x // 10] + x % 10
    digitSum[x] = s
    groups[s].append(x)

# print(max(len(lst) for lst in groups.values()))  # 365

class Solution1:
    def countArrays(self, digitSum: list[int]) -> int:
        f = [0] * (MAX_V + 1)
        f[0] = 1
        for d in digitSum:
            s = list(accumulate(f, func=lambda x, y: x + y % MOD))
            nf = [0] * (MAX_V + 1)
            for x in groups[d]:
                nf[x] = (nf[x] + s[x]) % MOD
            f = nf
        return sum(f) % MOD

class Solution2:
    def countArrays(self, digitSum: list[int]) -> int:
        f = [0] * (MAX_V + 1)
        f[0] = 1
        pre = 0
        for cur in digitSum:
            s = idx = 0
            arr = groups[pre]
            m = len(arr)
            for x in groups[cur]:
                while idx < m and arr[idx] <= x:
                    s = (s + f[arr[idx]]) % MOD
                    idx += 1
                f[x] = s % MOD
            pre = cur
        # 注意只有 x in groups[pre] 的數字才需要計算，其他數字不會被更新到。
        return sum(f[x] for x in groups[pre]) % MOD

# Solution = Solution1
Solution = Solution2
# @lc code=end

