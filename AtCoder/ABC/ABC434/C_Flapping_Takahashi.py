def solve():
    N, H = map(int, input().split())
    limits = [tuple(map(int, input().split())) for _ in range(N)]

    pt = 0
    L = R = H
    for t, l, r in limits:
        d = t - pt
        L = max(L - d, 1)  # 展開下界，截斷為 >= 1（高度 > 0）
        R = R + d  # 展開上界
        if l > R or r < L:  # 交集為空 → 無解
            print("No")
            return
        L = max(L, l)  # 與目標下界取交集
        R = min(R, r)  # 與目標上界取交集
        pt = t
    print("Yes")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
