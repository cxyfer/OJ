import math
from collections import defaultdict

N, Q = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

# 回滾莫隊 (只加不刪)
cnt = defaultdict(int)
max_val = -1
def add(x: int) -> None:
    global max_val
    cnt[x] += 1
    max_val = max(max_val, cnt[x] * x)

BLK_SZ = math.ceil(N / math.sqrt(Q * 2))

ans = [-1] * Q
queries = []  # (bid, l, r, qid)
for qid in range(Q):
    l, r = map(int, input().split())
    l -= 1  # 0-indexed, [l, r]
    r -= 1
    # 大區間離線，確保 l 和 r 不在同一個 block 中
    if r - l + 1 > BLK_SZ:
        queries.append((l // BLK_SZ, l, r, qid))
        continue
    # 小區間暴力
    for x in A[l: r + 1]:
        add(x)
    ans[qid] = max_val
    # 重置
    cnt.clear()
    max_val = -1

queries.sort(key=lambda x: (x[0], x[2]))  # sort by block index and right index
for i, (bid, ql, qr, qid) in enumerate(queries):
    l0 = (bid + 1) * BLK_SZ
    if i == 0 or bid > queries[i - 1][0]:  # 遍歷到一個新的 block
        r = l0  # 右端點移動的起点
        cnt.clear()
        max_val = -1

    # 右端點從 r 向右移動到 qr（包含 qr）
    while r <= qr:
        add(A[r])
        r += 1

    tmp_max_val = max_val

    # 左端點從 l0 向左移動到 ql（不包含 l0）
    for x in A[ql: l0]:
        add(x)
    ans[qid] = max_val

    # 回滚
    max_val = tmp_max_val
    for x in A[ql: l0]:
        cnt[x] -= 1

print(*ans, sep='\n')