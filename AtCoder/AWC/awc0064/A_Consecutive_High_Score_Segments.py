from itertools import groupby


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    print(sum(v for v, _ in groupby(A, key=lambda x: x >= k)))


if __name__ == "__main__":
    solve()
