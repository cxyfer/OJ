def solve():
    g, m, d, k, v = map(int, input().split())

    # 浮點數會有精度誤差，所以直接用分數來表示
    t1 = (k + (g - d * k), 1) if g >= d * k else (g, d)
    t2 = (m - g, v)

    print("Yes" if t1[0] * t2[1] <= t2[0] * t1[1] else "No")


if __name__ == "__main__":
    solve()
