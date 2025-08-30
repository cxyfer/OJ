import math

import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

N, Q = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

cnt0 = [0] * (N + 1)
for x in A:
    if x <= N: cnt0[x] += 1
mex0 = 0
while cnt0[mex0] > 0:
    mex0 += 1

# 回滾莫隊（只減不加）
cnt = [0] * (N + 1)
mex = 0
def delete(x: int) -> None:
    global mex
    if x > N:  # 大於 N 的數字不會影響 mex
        return
    cnt[x] -= 1
    if cnt[x] == 0:
        mex = min(mex, x)

BLK_SZ = math.ceil(N / math.sqrt(Q * 2))
# BLK_SZ = math.sqrt(N)

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
    for i in range(N + 1):
        cnt[i] = 0
    mex = 0
    for i in range(l, r + 1):
        if A[i] <= N: cnt[A[i]] += 1
    while cnt[mex] > 0:  # 這裡最多移動 BLK_SZ 次
        mex += 1
    ans[qid] = mex

queries.sort(key=lambda x: (x[0], -x[2]))  # sort by block index and right index
for i, (bid, ql, qr, qid) in enumerate(queries):
    l0 = bid * BLK_SZ
    if i == 0 or bid > queries[i - 1][0]:  # 遍歷到一個新的 block
        # 複製 cnt0 到 cnt
        for i in range(N + 1):
            cnt[i] = cnt0[i]
        mex = mex0
        r = N - 1  # 右端點移動的起點
        # 左端點刪到 l0 (不包含 l0)
        for i in range(0, l0):
            delete(A[i])

    # 右端點從 r 移動到 qr (不包含 qr)
    while qr < r:
        delete(A[r])
        r -= 1
    tmp_mex = mex
    # 左端點從 l0 移動到 ql (不包含 ql)
    for i in range(l0, ql):
        delete(A[i])
    ans[qid] = mex

    # 回滾
    mex = tmp_mex
    for i in range(l0, ql):
        if A[i] <= N: cnt[A[i]] += 1

print('\n'.join(map(str, ans)))