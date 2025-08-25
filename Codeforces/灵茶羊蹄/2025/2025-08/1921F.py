"""
基本知識：帶權前綴和

1. 離線分組
最壞情況下需要計算有 1 組長度為 n 、2 組 n / 2、3 組 n / 3 ... √q 個 n / √q 的前綴和，
時間複雜度為 O(n √q)

2. 分塊
對於 d 太大的情況，顯然暴力做也不會太差，因此可以分塊，小區間預處理，大區間暴力
"""

from collections import defaultdict
import math

t = int(input())

def solve1():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))

    ans = [-1] * q
    mp = defaultdict(lambda: defaultdict(list))
    for qid in range(q):
        s, d, k = map(int, input().split())
        s -= 1  # 0-indexed
        mp[d][s % d].append((qid, s, k))

    for d, ms in mp.items():
        for m, qs in ms.items():
            ln = (n - 1 - m) // d + 1
            s1 = [0] * (ln + 1)  # 普通前綴和
            s2 = [0] * (ln + 1)  # 帶權前綴和
            for i in range(ln):
                s1[i + 1] = s1[i] + A[m + i * d]
                s2[i + 1] = s2[i] + A[m + i * d] * (i + 1)
            for qid, s, k in qs:
                l = (s - m) // d
                r = l + k - 1
                ans[qid] = s2[r + 1] - s2[l] - l * (s1[r + 1] - s1[l])
    print(*ans)

def solve2():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    BLK_SZ = int(math.sqrt(q)) + 1

    s1 = [[0] * (n + BLK_SZ) for _ in range(BLK_SZ)]
    s2 = [[0] * (n + BLK_SZ) for _ in range(BLK_SZ)]
    for d in range(1, BLK_SZ):
        for i in range(n):
            s1[d][i + d] = s1[d][i] + A[i]
            s2[d][i + d] = s2[d][i] + A[i] * (i // d + 1)

    ans = []
    for _ in range(q):
        s, d, k = map(int, input().split())
        s -= 1  # 0-indexed
        if d >= BLK_SZ:
            cur = 0
            for i in range(k):
                cur += A[s + i * d] * (i + 1)
            ans.append(cur)
        else:
            r = s + k * d
            ans.append(s2[d][r] - s2[d][s] - (s // d) * (s1[d][r] - s1[d][s]))
    print(*ans)

for _ in range(t):
    # solve1()
    solve2()