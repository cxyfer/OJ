from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from string import *
from typing import *

"""
## Q3. 構造

對於網格比較大的情況，可以構造出數量為 0~B 區塊，之後對 k 進行 B 進位拆分，再用類似連接電路的方式貢獻到答案中。
例如用 2 x 4 的區塊做二進位拆分，對於 n, m = 200 的情況約可以構造出 1e18 內的任意數字。
```
.?...
.#
..
..?..
 .#
 ..
 ..
```

但這題的網格太小了，反而不能任意構造，不過 k 也只有 1~4，因此可以直接分類討論所有情況。
- k = 1 時，即前幾周的 [3963. Create Grid With Exactly One Path](https://leetcode.com/problems/create-grid-with-exactly-one-path/)
- 使用 2 x k 或 k x 2 的區塊可以構造出 1~4 的任意數字
- 若 k = 4 則可以重疊兩個 2 x 2 的區塊，並連接到右下角，需要至少 3 x 3 的網格
"""


class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        ans = [["#"] * n for _ in range(m)]

        def connect(r1: int, c1: int, r2: int = m - 1, c2: int = n - 1) -> None:
            for c in range(c1, c2 + 1):
                ans[r1][c] = "."
            for r in range(r1, r2 + 1):
                ans[r][c2] = "."

        if k == 1:
            for c in range(n):
                ans[0][c] = "."
            for r in range(m):
                ans[r][n - 1] = "."
        elif m >= 2 and n >= k:  # 2 x k
            for r in range(2):
                for c in range(k):
                    ans[r][c] = "."
            connect(1, k - 1)
        elif n >= 2 and m >= k:  # k x 2
            for r in range(k):
                for c in range(2):
                    ans[r][c] = "."
            connect(k - 1, 1)
        elif k == 4 and m >= 3 and n >= 3:  # Example 2
            for b in range(2):
                for r in range(b, b + 2):
                    for c in range(b, b + 2):
                        ans[r][c] = "."
            connect(2, 2)
        else:
            return []

        return ["".join(row) for row in ans]


def check(grid: list[str]):
    m, n = len(grid), len(grid[0])

    f = [[0] * n for _ in range(m)]
    f[0][0] = 1 if grid[0][0] == "." else 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                f[i][j] = 0
            else:
                if i > 0:
                    f[i][j] += f[i - 1][j]
                if j > 0:
                    f[i][j] += f[i][j - 1]
    return f[m - 1][n - 1]


sol = Solution()

for m in range(1, 11):
    for n in range(1, 11):
        for k in range(1, 5):
            grid = sol.createGrid(m, n, k)
            if not grid:
                continue
            assert check(grid) == k, f"m={m}, n={n}, k={k}, grid={grid}"