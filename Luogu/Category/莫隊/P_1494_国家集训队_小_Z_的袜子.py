import math
from collections import defaultdict

import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

# Mo's algorithm
cnt = defaultdict(int)
cur = 0
def add(x: int) -> None:
    global cur
    cur -= cnt[x] * (cnt[x] - 1) // 2
    cnt[x] += 1
    cur += cnt[x] * (cnt[x] - 1) // 2

def delete(x: int) -> None:
    global cur
    cur -= cnt[x] * (cnt[x] - 1) // 2
    cnt[x] -= 1
    cur += cnt[x] * (cnt[x] - 1) // 2

BLK_SZ = math.ceil(N / math.sqrt(M * 2))

ans = [(-1, -1)] * M
queries = []  # (bid, l, r, qid)
for qid in range(M):
    l, r = map(int, input().split())
    l -= 1  # 0-indexed, [l, r]
    r -= 1
    # 大區間離線，確保 l 和 r 不在同一個 block 中
    if r - l > BLK_SZ:
        queries.append((l // BLK_SZ, l, r, qid))
        continue
    # 小區間暴力
    for x in A[l: r + 1]:
        add(x)
    den = (r - l + 1) * (r - l) // 2
    ans[qid] = (cur, den)
    # 重製
    cnt.clear()
    cur = 0

queries.sort(key=lambda x: (x[0], x[2]))  # sort by block index and right index
l, r = 0, -1
for i, (bid, ql, qr, qid) in enumerate(queries):
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
    den = (r - l + 1) * (r - l) // 2
    ans[qid] = (cur, den)

for num, den in ans:
    if den == 0:
        print("0/1")
        continue
    g = math.gcd(num, den)
    print(f"{num // g}/{den // g}")