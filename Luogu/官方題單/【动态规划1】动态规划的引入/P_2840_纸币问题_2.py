"""
P2840 纸币问题_2
https://www.luogu.com.cn/problem/P2840
背包DP模板題：求「排列」方案數
"""

import sys
from functools import cache

sys.setrecursionlimit(int(2e4))
MOD = int(1e9) + 7


def solve1():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    A.sort()

    @cache
    def dfs(x):
        if x == 0:
            return 1
        res = 0
        for a in A:
            if x - a < 0:
                break
            res = (res + dfs(x - a)) % MOD
        return res

    print(dfs(k))


def solve2():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    A.sort()

    f = [1] + [0] * k
    for i in range(1, k + 1):
        for a in A:
            if i - a < 0:
                break
            f[i] = (f[i] + f[i - a]) % MOD
    print(f[k])


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
