"""
P8085 [COCI 2011/2012 #4] KRIPTOGRAM
https://www.luogu.com.cn/problem/P8085
Sliding Window + Hash

由於有對應關係，明文中大小為 m 的子陣列和密文中，相同元素的距離是相同的
使用滑動窗口維護這個轉換後的子陣列，並且使用雜湊值判斷是否相同
"""
from collections import defaultdict, deque
from random import randint

A = list(input().split())
B = list(input().split())
A.pop()
B.pop()
n, m = len(A), len(B)

MOD = 1070777777
BASE = randint(int(1e8), int(1e9))
P = [1] + [0] * m
for i in range(m):
    P[i + 1] = P[i] * BASE % MOD

# 計算密文轉換後的距離陣列，並且計算雜湊值
pos = defaultdict(list)
d2 = [-1] * m
h0 = 0
for i, b in enumerate(B):
    if pos[b]:
        d2[i] = i - pos[b][-1]
    pos[b].append(i)
    h0 = (h0 * BASE + d2[i]) % MOD

# 滑動窗口
pos = defaultdict(deque)
d1 = [-1] * n
h = 0
for r, x in enumerate(A):
    # h = (h * BASE + d1[r]) % MOD
    # 出窗口
    if r - m >= 0:
        # 消除出窗口的元素的貢獻，注意這時候 h 計算還是 A[r-m...r-1] 的雜湊值
        y = A[r - m]
        h = (h - d1[r - m] * P[m - 1]) % MOD
        pos[y].popleft()
        # 會影響到窗口內的 d1 值
        if pos[y]:
            idx = pos[y][0]
            h = (h - d1[idx] * P[r - idx - 1]) % MOD
            d1[idx] = -1
            h = (h + d1[idx] * P[r - idx - 1]) % MOD
    # 入窗口
    if pos[x]:
        d1[r] = r - pos[x][-1]
    pos[x].append(r)
    h = (h * BASE + d1[r]) % MOD

    if h == h0:
        # 左端點為 r - m + 1，輸出為 1-indexed
        print(r - m + 2)
        break