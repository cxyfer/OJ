def solve():
    n, m, k = map(int, input().split())

    grid = [input() for _ in range(n)]
    ans = float('inf')
    for i in range(n):
        cnt = [0] * m
        for j in range(i, n):
            for c in range(m):
                cnt[c] += grid[j][c] == '1'
            s = left = 0
            for right in range(m):
                s += cnt[right]
                while s - cnt[left] >= k:
                    s -= cnt[left]
                    left += 1
                if s >= k:
                    ans = min(ans, (right - left + 1) * (j - i + 1))
    print(ans if ans != float('inf') else 0)

if __name__ == '__main__':
    solve()