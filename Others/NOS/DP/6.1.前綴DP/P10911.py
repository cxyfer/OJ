"""
P10911 [蓝桥杯 2024 国 B] 数位翻转
https://www.luogu.com.cn/problem/P10911
前綴DP

對增加的貢獻取 m 段最大子陣列和即可。
"""
def flip(x):
    return int(bin(x)[2:][::-1], 2)

def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = [flip(x) - x for x in A]  # 增加的貢獻

    # f[i][j][0/1] 表示在前 i+1 個數中選取 j 段的最大貢獻，0/1 表示是否選取第 i 個數
    f = [[[0, 0] for __ in range(m + 1)] for _ in range(2)]
    for i, x in enumerate(B):
        curr, prev = f[i & 1], f[(i - 1) & 1]
        for j in range(1, m + 1):
            curr[j][0] = max(prev[j][0], prev[j][1])
            curr[j][1] = max(prev[j - 1][0], prev[j][1]) + x
    ans = 0
    for j in range(m + 1):
        ans = max(ans, f[(n - 1) & 1][j][0], f[(n - 1) & 1][j][1])
    ans += sum(A)
    print(ans)

solve()