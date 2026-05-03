"""
abc410_g Longest Chord Chain
https://atcoder.jp/contests/abc410/tasks/abc410_g
破環成鏈 + LIS

若干個個弦不相交，等同 l1 < l2 < ... < lk ，且 r1 > r2 > ... > rk
此即為二維 LIS 問題，但第二維求的是 LDS，這可以通過將 r 取負來解決。
"""

from bisect import bisect_left


def solve():
    n = int(input())
    A = []
    for _ in range(n):
        l, r = map(int, input().split())
        l, r = min(l, r), max(l, r)
        A.append((l, r))
        A.append((r, l + (n << 1)))
    A.sort()
    f = []
    for _, r in A:
        idx = bisect_left(f, -r)
        if idx == len(f):
            f.append(-r)
        else:
            f[idx] = -r
    print(len(f))


if __name__ == "__main__":
    solve()
