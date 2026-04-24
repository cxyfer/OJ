"""
P8218 【深进1.例1】求区间和
https://www.luogu.com.cn/problem/P8218
"""

from itertools import accumulate


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    s = list(accumulate(A, initial=0))
    q = int(input())
    ans = []
    for _ in range(q):
        l, r = map(int, input().split())
        ans.append(s[r] - s[l - 1])
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
