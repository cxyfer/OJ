import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q4. 字串合併
有一個經典問題是給定一個字串陣列，求出所有字串的合併後字串的字典序最大的字串。
則對於兩個字串 x, y，我們可以比較 xy 和 yx 的字典序，如果 xy > yx，則 x 應該在 y 前面。
本題同理，我們可以寫一個自定義的比較函數，根據1和0的數量轉換為字串，然後比較 xy 和 yx 的字典序。

但這樣的比較很耗時，因此我們可以利用數學性質來優化。
由於每個字串都只由 a 個 1 和 b 個 0 組成，因此我們可以分類討論：
- 如果 x.a == y.a 且 x.b == y.b，則 x 和 y 是相等的
- 如果 x.b == 0 ，則 xy 組合後所有的 0 都在最後面，因此 xy > yx；反之亦然。
- 如果 x.a > y.a ，則 xy 的前綴 1 會比 yx 的前綴 1 多，因此 xy > yx；反之亦然。
- 如果 x.a == y.a 且 x.b < y.b，則 xy 的前綴 1 後會接比較少的 0，因此 xy > yx；反之亦然。

但還能注意到，只要 x.b = 0，則 x 理應排在前面，因此我們可以先處理這些元素對前綴 1 的貢獻，然後再處理其他元素。
此時其他元素只需根據 (-a, b) 來排序即可。
"""

MOD = int(1e9 + 7)
MAX_N = int(2e5 + 5)
pow2 = [1] * MAX_N
for i in range(1, MAX_N):
    pow2[i] = pow2[i - 1] * 2 % MOD


class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        segs = []
        for a, b in zip(nums1, nums0):
            segs.append((a, b))

        def cmp(x, y):
            # xy = '1' * x[0] + '0' * x[1] + '1' * y[0] + '0' * y[1]
            # yx = '1' * y[0] + '0' * y[1] + '1' * x[0] + '0' * x[1]
            # if xy == yx:
            #     return 0
            # return -1 if xy > yx else 1
            if x[0] == y[0] and x[1] == y[1]:
                return 0
            if x[1] == 0:  # 只有 y 有 0，故 0 一定是在 xy 的最後面，xy > yx
                return -1
            if y[1] == 0:  # 只有 x 有 0，故 0 一定是在 yx 的最後面，xy < yx
                return 1
            if x[0] > y[0] or (x[0] == y[0] and x[1] < y[1]):  # xy > yx
                return -1
            return 1

        segs.sort(key=cmp_to_key(cmp))
        ans = 0
        for a, b in segs:
            ans = (ans * pow2[a] + (pow2[a] - 1)) % MOD
            ans = (ans * pow2[b]) % MOD
        return ans


sol = Solution()
print(sol.maxValue(nums1=[1, 2], nums0=[1, 0]))  # 14
print(sol.maxValue(nums1=[3, 1], nums0=[0, 3]))  # 120