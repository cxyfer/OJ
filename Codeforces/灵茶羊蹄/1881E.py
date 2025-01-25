"""
令 f[i] 表示使 A[i:] 合法所需的最少刪除數，則對於每個元素 A[i] 可以選擇刪除或不刪除
- 若刪除，則可以從 f[i + 1] 轉移過來，刪除次數為 1 + f[i + 1]
- 若不刪除，則這個 A[i] 會是一個 Block 的開頭，根據定義，這個 Block 的長度為 A[i] + 1，
  因此可以從 f[i + A[i] + 1] 轉移過來，刪除次數為 f[i + A[i] + 1] + 1

用 @cache 做 Memoization 會 MLE
"""
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    # f[i] 表示使 A[i:] 合法所需的最少刪除數
    f = [0] * (n + 1) + [float('inf')]
    for i in range(n - 1, -1, -1):
        f[i] = min(1 + f[i + 1], f[min(n + 1, i + A[i] + 1)])
    print(f[0])