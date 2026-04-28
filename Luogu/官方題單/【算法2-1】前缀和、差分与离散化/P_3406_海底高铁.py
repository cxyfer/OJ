from itertools import pairwise, accumulate


def solve():
    n, m = map(int, input().split())
    cities = list(map(lambda x: int(x) - 1, input().split()))
    roads = [tuple(map(int, input().split())) for _ in range(n - 1)]
    assert len(cities) == m
    assert len(roads) == n - 1

    diff = [0] * n
    for a, b in pairwise(cities):
        l, r = min(a, b), max(a, b)
        diff[l] += 1
        diff[r] -= 1

    s = list(accumulate(diff))

    ans = 0
    for x, (a, b, c) in zip(s, roads):
        ans += min(x * a, x * b + c)
    print(ans)


if __name__ == "__main__":
    solve()
