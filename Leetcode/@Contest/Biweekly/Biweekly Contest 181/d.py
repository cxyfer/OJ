import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q4. ||二分搜尋||

首先注意到我們只需要關心偶數的位置，因此可以將 nums 中的偶數位置記錄下來，記做 evens 和 idxs
又 nums 是遞增的，因此可以二分找到區間 [l, r] 對應的 evens 中的索引，記做 idx1 和 idx2
問題轉換成：刪除 evens[idx1], evens[idx1 + 1], ..., evens[idx2] 後，第 k 個未被移除的偶數是多少？

令 f(idx) 表示 [2, 4, ..., evens[idx] - 2] 有幾個未被移除的偶數，則 f 會隨著 idx 增加而遞增
因此可以考慮對 idx1 到 idx2 之間進行二分搜尋，找到最小的 idx 使得 f(idx) >= k
f(idx) = 原本的偶數數量 - 移除的偶數數量 = (evens[idx] // 2) - (idx - idx1 + 1)

第一個滿足 f(idx) >= k 的 idx 就是我們要找的答案，
所求為 (k + 前面被刪除的偶數數量) * 2，其中 前面被刪除的偶數數量 = idx - idx1 + 1

上面是甚麼傻逼寫法，直接對答案二分不香嗎？
"""

class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        evens = []
        idxs = []
        for i, x in enumerate(nums):
            if x & 1 == 0:
                evens.append(x)
                idxs.append(i)
                

        q = len(queries)
        ans = [-1] * q
        for qid, (l, r, k) in enumerate(queries):
            idx1 = bisect_left(idxs, l)
            idx2 = bisect_right(idxs, r) - 1

            # 不需要移除任何偶數（區間為空） 或是 光前面的偶數就夠 k 個了）
            if idx1 > idx2 or evens[idx1] // 2 - 1 >= k:
                ans[qid] = k * 2
                continue

            # [2, 4, ..., evens[mid]] 有幾個未被移除的偶數
            # 因為 evens[mid] 一定會被移除，實際上是 [2, 4, ..., evens[mid] - 2] 有幾個未被移除的偶數
            def check(mid):
                return (evens[mid] // 2) - (mid - idx1 + 1)

            left, right = idx1, idx2
            while left <= right:
                mid = (left + right) // 2
                if check(mid) >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            k += (left - 1) - idx1 + 1  # 移除的偶數數量 = 需要補償的偶數數量
            ans[qid] = k * 2
        return ans

sol = Solution()
print(sol.kthRemainingInteger(nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]))  # [2,6,6]
print(sol.kthRemainingInteger(nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]))  # [6,2,12]
print(sol.kthRemainingInteger(nums = [3,6], queries = [[0,1,1],[1,1,3]]))  # [2,8]
print(sol.kthRemainingInteger(nums = [15], queries = [[0,0,10]])) # [20]
print(sol.kthRemainingInteger(nums = [5,15,18,26], queries = [[1,3,10],[2,3,26]]))  # [22,56]
print(sol.kthRemainingInteger(nums = [30,41,46,49,61,72,76,80,88], queries = [[2,7,34],[2,5,72]]))  # [70,148]