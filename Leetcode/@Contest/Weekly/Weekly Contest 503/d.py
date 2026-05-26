import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


"""
Q4: 根號分塊 + lazy tag

看似可以用 Lazy Segment Tree，但操作 2 需要查詢整個區間的 Counter，且值域為 1e5，因此對於樹上每個 Node 都維護一個 Counter 是不太可能的。

但我們可以借用 lazy tag 的概念，使用根號分塊，對每個區塊維護一個 Counter 和一個 lazy tag，
其中 cnts[b][x] 表示區塊 b 中值為 x 的元素數量，lazy[b] 表示區塊 b 中所有元素的增量。
如此在操作 1 時，對於完整的區塊只需要更新 lazy tag，對於不完整的部分則是更新 Counter 和 nums2 的值。
在操作 2 時，對於每個區塊的 Counter 查詢 tot - lazy[b] - nums1[i] 的數量，最後加總得到答案。
"""

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums2)

        B = math.isqrt(n) + 1
        SZ = math.ceil(n / B)

        # cnts[b][x] 表示區塊 b 中值為 x 的元素數量
        # lazy[b] 表示區塊 b 中所有元素的增量
        cnts = [defaultdict(int) for _ in range(SZ)]
        lazy = [0] * SZ
        for i, v in enumerate(nums2):
            b = i // B
            cnts[b][v] += 1

        # 小區間直接暴力修改 nums2 和 Counter
        def update(l: int, r: int, val: int) -> None:
            b = l // B
            cnt = cnts[b]
            for i in range(l, r + 1):
                x = nums2[i]
                cnt[x] -= 1
                y = x + val
                cnt[y] += 1
                nums2[i] = y

        ans = []
        for query in queries:
            op, *args = query
            if op == 1:
                l, r, val = args
                bl, br = l // B, r // B
                if bl == br:
                    update(l, r, val)
                    continue
                # 不完整的區塊
                update(l, min(n, (bl + 1) * B) - 1, val)
                update(br * B, r, val)
                # 對於完整的區塊只需要更新 lazy tag
                for b in range(bl + 1, br):
                    lazy[b] += val
            else:
                tot = args[0]
                res = 0
                for b, cnt in enumerate(cnts):
                    for x in nums1:
                        res += cnt[tot - lazy[b] - x]
                ans.append(res)
        return ans

sol = Solution()
print(sol.numberOfPairs(nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]))  # [2,1]
print(sol.numberOfPairs(nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]]))  # [2,6]
print(sol.numberOfPairs(nums1 = [2,5,8,4], nums2 = [1,3,8], queries = [[2,9],[1,1,2,1],[2,10]]))  # [1,0]