"""
abc410_g Longest Chord Chain
https://atcoder.jp/contests/abc410/tasks/abc410_g
破環成鏈 + LIS

若干個個弦不相交，等同 l1 < l2 < ... < lk ，且 r1 > r2 > ... > rk
此即為二維 LIS 問題，但第二維求的是 LDS，這可以通過將 r 取負來解決。
"""

from bisect import bisect_left


def solve1():
    n = int(input())

    A = []
    for _ in range(n):
        l, r = map(int, input().split())
        l, r = min(l, r), max(l, r)
        A.append((l, r))
        A.append((r, l + (n << 1)))

    # 第一維 LIS，第二維 LDS
    A.sort()
    f = []
    for _, r in A:
        idx = bisect_left(f, -r)
        if idx == len(f):
            f.append(-r)
        else:
            f[idx] = -r
    print(len(f))


def solve2():
    n = int(input())

    pos = [-1] * (n << 1)
    for _ in range(n):
        l, r = map(lambda x: int(x) - 1, input().split())
        l, r = min(l, r), max(l, r)
        pos[l] = r
        pos[r] = l + (n << 1)

    f = []
    for r in pos:
        idx = bisect_left(f, -r)
        if idx == len(f):
            f.append(-r)
        else:
            f[idx] = -r
    print(len(f))


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
