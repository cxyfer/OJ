import math
from collections import defaultdict

N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

# Mo's algorithm
cnt = defaultdict(int)
cur = 0
def add(x: int) -> None:
    global cur
    cnt[x] += 1
    if cnt[x] == 1:
        cur += 1

def delete(x: int) -> None:
    global cur
    cnt[x] -= 1
    if cnt[x] == 0:
        cur -= 1

BLK_SZ = math.pow(N, 2.0 / 3.0)

qid = ts = 0
queries = []  # (l, r, ts, qid)
records = []  # (pos, val)
for _ in range(M):
    op, *args = input().split()
    if op == 'Q':
        l, r = map(int, args)
        r -= 1  # [l, r]
        queries.append([l, r, ts, qid])
        qid += 1
    else:
        pos, val = map(int, args)
        records.append([pos, val])
        ts += 1

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
    ans[qid] = cur

print(*ans, sep='\n')