"""
F - 小L的抽卡
https://ac.nowcoder.com/acm/contest/95337/F

Divide and Conquer + Knapsack DP
Source: https://www.luogu.com.cn/problem/P6240 (貓樹)

先不管詢問，考慮如何計算一段區間的結果，這是類似 01 背包的機率 DP 問題。
定義 f[i][j] 表示在前 i 個物品中，抽中的數量對 k 取模後為 j 的機率。
考慮第 i 個有沒有抽到的兩種情況，有遞迴式：
f[i][j] = f[i - 1][j] * (1 - p[i]) + f[i - 1][(j - 1) % k] * p[i]

Knapsack DP 有容易合併的性質，所以可以離線 + 分治來做。
- 對於穿過中間點 mid 的詢問，可以計算從中點往左和往右的 DP 結果，然後合併。
- 對於詢問區間完全在左邊或右邊的，往下分治處理。

每個物品會出現在 O(log n) 個分治區間內，每次出現計算背包時會貢獻 O(C) 的時間複雜度，總共有 N 個物品。
每次詢問需要花 O(C) 的時間複雜度，總共有 Q 個詢問。
所以總時間複雜度為 O(N * C * log N + Q * C)。

時間限制有點緊張
"""
MOD = int(1e9 + 7)
n, q, k = map(int, input().split())
P = [0] + list(map(lambda x: pow(x, MOD - 2, MOD), map(int, input().split())))
queries = [tuple(map(int, input().split())) for _ in range(q)]

ans = [-1] * q
qids = []
for qid, (l, r, c) in enumerate(queries):
    if l == r:
        if c == 0:
            ans[qid] = (1 - P[l]) % MOD
        elif c == 1:
            ans[qid] = P[l]
        else:
            ans[qid] = 0
    else:
        qids.append(qid)

fl = [[0] * k for _ in range(n + 1)]
fr = [[0] * k for _ in range(n + 1)]

def solve(left, right, qids) -> None:
    if len(qids) == 0:
        return
    mid = (left + right) // 2
    ql, qr, qm = [], [], []
    for qid in qids:
        l, r, c = queries[qid]
        if l <= mid and r > mid:
            qm.append(qid)
        elif r <= mid:
            ql.append(qid)
        else:
            qr.append(qid)
    if len(qm) > 0:
        fl[mid + 1][0] = fr[mid][0] = 1
        for c in range(1, k):
            fl[mid + 1][c] = fr[mid][c] = 0
        # fl: [left, mid]
        for i in range(mid, left - 1, -1):
            p = P[i]
            prev, curr = fl[i + 1], fl[i]
            for c in range(k):
                curr[c] = (prev[c] * (1 - p) + prev[(c - 1) % k] * p) % MOD
        # fr: [mid + 1, right]
        for i in range(mid + 1, right + 1):
            p = P[i]
            prev, curr = fr[i - 1], fr[i]
            for c in range(k):
                curr[c] = (prev[c] * (1 - p) + prev[(c - 1) % k] * p) % MOD
        for qid in qm:
            l, r, c = queries[qid]
            res = 0
            fll, frr = fl[l], fr[r]
            for cl in range(k):  # 枚舉左側抽中的數量 cl
                res += fll[cl] * frr[(c - cl) % k]
                res %= MOD
            ans[qid] = res
    solve(left, mid, ql)
    solve(mid + 1, right, qr)

solve(1, n, qids)
print(*ans, sep='\n')