from functools import cache


def solve1():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    @cache
    def dfs(x):
        if x == 0:
            return 0
        res = float("inf")
        for a in A:
            if x - a < 0:
                break
            res = min(res, dfs(x - a) + 1)
        return res

    print(dfs(k))


def solve2():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    A.sort()

    f = [0] + [float("inf")] * k
    for i in range(1, k + 1):
        for a in A:
            if i - a < 0:
                break
            f[i] = min(f[i], f[i - a] + 1)
    print(f[k])


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
