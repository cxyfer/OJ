"""
AWC0104E Warehouse Inventory Management
https://atcoder.jp/contests/awc0104/tasks/awc0104_e
根號分治
請使用 Python (Codon 0.19.3) 提交，否則會 TLE

所求為 sum(max(0, C[i]))，其中 C[i] = B[i] - A[i]，且每次操作會對一段區間的 C[i] 加上或減去一個值。

將 C 分成長度為 B 的若干個 block，每個 block 內維護：
1. 排序後的 C 值
2. 排序後的 C 值的前綴和
3. 一個 lazy 值，表示整個 block 的 C 值都加上 lazy。

在計算貢獻時，需要找到所有 C[i] + lazy >= 0 的值，
由於 block 內的 C 已經排序，因此可以使用二分搜尋找到第一個 C[i] + lazy >= 0 的位置，然後利用前綴和計算 sum(max(0, C[i]))。

在操作時，對於完整的 block，只需要更新 lazy 值即可，對於不完整的 block，則需要直接更新 C 值並重新建構排序與前綴和。

對於每次操作：
- 更新完整的 block 需要 O(1) 的時間，每次操作最多只會更新 O(n / B) 個完整的 block
- 更新不完整的 block 需要 O(B log B) 的時間，每次操作最多只會更新 2 個不完整的 block
- 對於每個 block 計算貢獻需要 O(log B) 的時間，每次操作最多需要計算 O(n / B) 個 block

因此總時間複雜度為 O((n / B) log B + B log B)，
B 取 sqrt(n) 時，總時間複雜度為 O(sqrt(n) log n)。

Codon 注意事項（踩過的坑）：
1. map(...) 在 Codon 中會被視為 Generator，不能直接解包，需先轉成 list。
2. [[] for _ in range(m)] 可能被推斷成 List[List[NoneType]]，巢狀 int list 要給 Codon 明確型別線索。
3. 使用巢狀函式自動捕獲函式內的可變狀態時，Codon 不一定能編譯，需顯式傳參或改用全域變數。因為懶得寫顯式傳參，所以這份程式使用全域變數。
"""

from bisect import bisect_left
from itertools import accumulate


n, q = list(map(int, input().split()))
C: list[int] = []
for _ in range(n):
    # a, b = map(int, input().split())
    a, b = list(map(int, input().split()))
    C.append(b - a)

# B = isqrt(n) + 1
B = int(n**0.5) + 1
m = (n + B - 1) // B  # ceil(n / B)

bucket: list[list[int]] = [[] for _ in range(m)]
presum: list[list[int]] = [[] for _ in range(m)]
lazy: list[int] = [0] * m
ans = sum(max(0, x) for x in C)


def build(b: int) -> None:
    l = b * B
    r = min(n, (b + 1) * B)
    bucket[b] = sorted(C[l:r])
    presum[b] = list(accumulate(bucket[b], initial=0))


def count(b: int) -> int:
    A = bucket[b]
    ps = presum[b]
    idx = bisect_left(A, -lazy[b])
    cnt = len(A) - idx
    return ps[-1] - ps[idx] + cnt * lazy[b]


def add(b: int, l: int, r: int, v: int) -> None:
    global ans
    ans -= count(b)
    for i in range(l, r + 1):
        C[i] += v
    build(b)
    ans += count(b)


for b in range(m):
    build(b)


for _ in range(q):
    op, l, r, v = list(map(int, input().split()))
    l, r = l - 1, r - 1
    if op == 2:
        v = -v

    bl, br = l // B, r // B
    if bl == br:
        add(bl, l, r, v)
    else:
        add(bl, l, (bl + 1) * B - 1, v)
        add(br, br * B, r, v)
        for b in range(bl + 1, br):
            ans -= count(b)
            lazy[b] += v
            ans += count(b)
    print(ans)
