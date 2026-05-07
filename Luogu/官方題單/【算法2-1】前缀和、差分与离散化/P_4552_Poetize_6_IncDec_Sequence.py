"""
P4552 [Poetize6] IncDec Sequence
https://www.luogu.com.cn/problem/P4552
差分思想
"""


def solve():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    diff = [0] * n
    for i in range(1, n):
        diff[i] = A[i] - A[i - 1]

    pos = sum(diff[i] for i in range(n) if diff[i] > 0)
    neg = sum(-diff[i] for i in range(n) if diff[i] < 0)

    print(max(pos, neg))
    print(abs(pos - neg) + 1)


if __name__ == "__main__":
    solve()
