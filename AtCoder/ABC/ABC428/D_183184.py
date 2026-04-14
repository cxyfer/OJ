from math import isqrt

pow10 = [1]
for _ in range(1, 20):
    pow10.append(pow10[-1] * 10)


def solve():
    C, D = map(int, input().split())

    ans = 0
    # 枚舉 y = C + x 的十進位長度
    # C + 1 <= (y = C + x) <= C + D
    for ln in range(len(str(C + 1)), len(str(C + D)) + 1):
        lo = max(C + 1, pow10[ln - 1])
        hi = min(C + D, pow10[ln] - 1)
        if lo > hi:
            continue
        # 得到滿足的 f(C, y) 的範圍 [L, R]
        L = C * pow10[ln] + lo
        R = C * pow10[ln] + hi
        # 計算滿足的 f(C, y) = k^2 的 k 的個數
        # 注意這裡直接用 floor(sqrt(R)) 以及 ceil(sqrt(L)) 會有精度問題
        k_max = isqrt(R)  # floor(sqrt(R))
        k_min = isqrt(L - 1) + 1  # ceil(sqrt(L))
        ans += max(0, k_max - k_min + 1)

    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
