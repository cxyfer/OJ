"""
P12316 [蓝桥杯 2024 国 C] 循环位运算
https://www.luogu.com.cn/problem/P12316
注意題目其實是問「最多」 k 次操作的結果，並不是「恰好」 k 次操作的結果
"""
U = (1 << 32) - 1

def solve():
    n, k = map(int, input().split())
    A = [int(input()) for _ in range(n)]
    # f[i][j] 表示考慮前 i 個數字，使用 j 次操作的最大和
    # f = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
    f = [[0] * (k + 1) for _ in range(2)]
    f[0][0] = 0
    for i, x in enumerate(A, 1):
        prev, curr = f[(i - 1) & 1], f[i & 1]
        for j in range(k + 1):
            curr[j] = prev[j] + x
            for d in range(1, min(32, j) + 1):  # 操作 32 次等於沒操作
                y = (x << d) & U | (x >> (32 - d))
                curr[j] = max(curr[j], prev[j - d] + y)
    print(max(f[n & 1]))

if __name__ == "__main__":
    solve()