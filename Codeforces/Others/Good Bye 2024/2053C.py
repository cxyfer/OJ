def solve():
    n, k = map(int, input().split())

    def dfs(ln):
        if ln < k:
            return 0
        return 2 * dfs(ln // 2) + (ln & 1)
    print(dfs(n) * (n + 1) // 2)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()