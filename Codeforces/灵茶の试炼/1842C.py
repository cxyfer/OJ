t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    mx = [-float("inf")] * (n + 1)

    """
    f[i] 表示在前 i 個數中，最多能刪除幾個數字
    f[i] = max(f[i - 1], max(f[j - 1] + i - j + 1))
    """
    f = [0] * (n + 1)
    for i, x in enumerate(A):
        f[i + 1] = max(f[i], i + mx[x])
        mx[x] = max(mx[x], f[i] - i + 1)
    print(f[n])