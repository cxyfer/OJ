from atcoder.fenwicktree import FenwickTree


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    bit = FenwickTree(n + 1)
    for x in A:
        ans += bit.sum(min(x + 1, n), n + 1)
        bit.add(x, 1)

    print(max(ans - k, 0))


if __name__ == "__main__":
    solve()
