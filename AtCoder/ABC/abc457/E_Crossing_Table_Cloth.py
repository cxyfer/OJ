from collections import defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate


def solve():
    n, m = map(int, input().split())
    intervals = [tuple(map(int, input().split())) for _ in range(m)]

    cnt = defaultdict(int)
    byL = defaultdict(list)  # L -> List[(R, idx)]
    byR = defaultdict(list)  # R -> List[(L, idx)]
    minR_at_L = [float("inf")] * (n + 1)

    for i, (l, r) in enumerate(intervals):
        cnt[(l, r)] += 1
        byL[l].append(r)
        byR[r].append(l)
        minR_at_L[l] = min(minR_at_L[l], r)

    for l, arr in byL.items():
        arr.sort()
    for r, arr in byR.items():
        arr.sort()

    # suf[x] = 所有 L >= x 的桌布中，最小的 R
    suf = list(accumulate(minR_at_L[::-1], min, initial=float("inf")))[::-1]

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        if s not in byL or t not in byR:
            print("No")
            continue

        if cnt[(s, t)] > 0:
            ok = False
            ok |= cnt[(s, t)] >= 2  # 有兩塊以上完全相同的 [s, t]
            ok |= suf[s + 1] <= t  # 存在 L > s 且 R <= t 的桌布
            ok |= suf[s] < t  # 存在 L >= s 且 R < t 的桌布
            print("Yes" if ok else "No")
            continue

        idx1 = bisect_right(byL[s], t) - 1
        idx2 = bisect_left(byR[t], s)

        if idx1 < 0 or idx2 == len(byR[t]):
            print("No")
            continue

        r = byL[s][idx1]
        l = byR[t][idx2]

        if l > r + 1:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    solve()
