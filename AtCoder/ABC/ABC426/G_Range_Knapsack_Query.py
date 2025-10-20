"""
Divide and Conquer + Knapsack DP
Source: https://www.luogu.com.cn/problem/P6240 (貓樹)

Knapsack DP 有容易合併的性質，所以可以離線 + 分治來做。
- 對於穿過中間點 mid 的詢問，可以計算從中點往左和往右的 DP 結果，然後合併。
- 對於詢問區間完全在左邊或右邊的，往下分治處理。

每個物品會出現在 O(log n) 個分治區間內，每次出現計算背包時會貢獻 O(C) 的時間複雜度，總共有 N 個物品。
每次詢問需要花 O(C) 的時間複雜度，總共有 Q 個詢問。
所以總時間複雜度為 O(N * C * log N + Q * C)。

因為 1e5 * 1e3 = 1e8，對 Python 來說有點勉強，需要考慮一些常數優化。
"""
from typing import List

N = int(input())
items = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

ans = [-1] * Q
MAX_C = 0
qids = []
for qid, (l, r, c) in enumerate(queries):
    if l == r:
        ans[qid] = items[l][1] if items[l][0] <= c else 0
    else:
        qids.append(qid)
        MAX_C = max(MAX_C, c)

fl = [[0] * (MAX_C + 1) for _ in range(N + 1)]
fr = [[0] * (MAX_C + 1) for _ in range(N + 1)]

def solve(left: int, right: int, qids: List[int]) -> None:
    if len(qids) == 0:
        return
    mid = (left + right) // 2
    ql, qr, qm = [], [], []
    C = 0
    for qid in qids:
        l, r, c = queries[qid]
        if l <= mid and r > mid:
            qm.append(qid)
            C = max(C, c)
        elif r <= mid:
            ql.append(qid)
        else:
            qr.append(qid)
    if len(qm) > 0:
        for c in range(MAX_C + 1):
            fl[mid + 1][c] = fr[mid][c] = 0
        # fl: [left, mid]
        for i in range(mid, left - 1, -1):
            w, v = items[i]
            prev, curr = fl[i + 1], fl[i]
            for c in range(C + 1):
                curr[c] = prev[c]
                if c >= w:
                    curr[c] = max(prev[c], prev[c - w] + v)
        # fr: [mid + 1, right]
        for i in range(mid + 1, right + 1):
            w, v = items[i]
            prev, curr = fr[i - 1], fr[i]
            for c in range(C + 1):
                curr[c] = prev[c]
                if c >= w:
                    curr[c] = max(curr[c], prev[c - w] + v)
        for qid in qm:
            l, r, c = queries[qid]
            mx = 0
            fll, frr = fl[l], fr[r]
            for cc in range(c + 1):
                mx = max(mx, fll[cc] + frr[c - cc])
            ans[qid] = mx
    solve(left, mid, ql)
    solve(mid + 1, right, qr)

solve(1, N, qids)
print(*ans, sep='\n')
