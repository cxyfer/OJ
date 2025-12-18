from functools import cache

def solve():
    n, k = map(int, input().split())

    if k >= 32:
        print(n.bit_count() + k - 1)
    else:
        @cache
        def dfs(i, j, carry):
            if (n >> i) == 0 and carry == 0:
                return j.bit_count()
            if j < 0:
                return float('inf')
            res = float('inf')
            b = (n >> i) & 1
            for t in range(2):
                tot = b + carry + t
                res = min(res, (tot & 1) + dfs(i + 1, j - t, tot >> 1))
            return res
        print(n.bit_count() + k - dfs(0, k, 0))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()