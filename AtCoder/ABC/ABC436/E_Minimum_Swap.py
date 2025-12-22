def solve():
    n = int(input())
    P = list(map(lambda x: int(x) - 1, input().split()))
    assert len(P) == n

    ans = 0
    vis = [False] * n
    for u in range(n):
        if vis[u]:
            continue
        cnt = 0
        while not vis[u]:
            vis[u] = True
            u = P[u]
            cnt += 1
        ans += cnt * (cnt - 1) // 2
    print(ans)

if __name__ == "__main__":
    solve()