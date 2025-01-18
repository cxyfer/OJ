from bisect import bisect_left, bisect_right

n, k, q = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]

# 為了方便二分，將 B 取轉置
B = [[-1] * n for _ in range(k)] # 初始化 B
for j in range(k):
    B[j][0] = A[0][j]
    for i in range(1, n):
        B[j][i] = B[j][i-1] | A[i][j]

for _ in range(q):
    m = int(input())
    # 維護一個區間 [L, R]，表示可能的答案範圍
    L, R = 0, n - 1
    for _ in range(m):
        r, o, c = input().split()
        r, c = int(r) - 1, int(c)
        if o == '<':
            idx = bisect_left(B[r], c) - 1
            R = min(R, idx)
        elif o == '>':
            idx = bisect_right(B[r], c)
            L = max(L, idx)
    # 輸出答案，記得轉換為 1-indexed
    print(L + 1 if L <= R and L <= n - 1 and R >= 0 else -1)