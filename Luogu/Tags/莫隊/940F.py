import math
from bisect import bisect_left

N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
B = A[:]  # 收集所有數字用於離散化

# 離線處理
qid = ts = 0
queries = []  # (l, r, ts, qid)
records = []  # (pos, val)
for _ in range(M):
    op, a, b = map(int, input().split())
    if op == 1:
        l, r = a - 1, b - 1  # [l, r]
        queries.append([l, r, ts, qid])
        qid += 1
    else:
        pos, val = a - 1, b
        B.append(val)
        records.append([pos, val])
        ts += 1

# 離散化
B = list(sorted(set(B)))
get_val = lambda x: bisect_left(B, x)
for i in range(N):
    A[i] = get_val(A[i])
for r in records:
    r[1] = get_val(r[1])

# Mo's algorithm
BLK_SZ = int(math.pow(N, 2.0 / 3.0))
cnt = [0] * (len(B) + 1)
cntcnt = [0] * (N + 1)
def add(x: int) -> None:
    cntcnt[cnt[x]] -= 1
    cnt[x] += 1
    cntcnt[cnt[x]] += 1

def delete(x: int) -> None:
    cntcnt[cnt[x]] -= 1
    cnt[x] -= 1
    cntcnt[cnt[x]] += 1

ans = [-1] * len(queries)
queries.sort(key=lambda x: (x[0] // BLK_SZ, x[1] // BLK_SZ, x[2]))
l, r, t = 0, -1, 0
for ql, qr, ts, qid in queries:
    while l > ql:
        l -= 1
        add(A[l])
    while r < qr:
        r += 1
        add(A[r])
    while l < ql:
        delete(A[l])
        l += 1
    while r > qr:
        delete(A[r])
        r -= 1
    while t < ts:
        pos, val = records[t]
        if l <= pos <= r:
            delete(A[pos])
            add(val)
        A[pos], records[t][1] = records[t][1], A[pos]
        t += 1
    while t > ts:
        t -= 1
        pos, val = records[t]
        if l <= pos <= r:
            delete(A[pos])
            add(val)
        A[pos], records[t][1] = records[t][1], A[pos]
    # 暴力求 mex
    mex = 1
    while cntcnt[mex] > 0:
        mex += 1
    ans[qid] = mex

print(*ans, sep='\n')