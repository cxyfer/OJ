"""
前後綴分解 + DP + 博弈論

首先要得到一個重要結論：Bob 的最優選擇是撤銷 Alice 的操作。
也就是在 k 為偶數時，所求就是原始的最大子陣列和。
而在 k 為奇數時，可以枚舉修改位置 i。
以前後綴分解處理以 i 為結尾的最大子陣列和 L[i]、以及以 i 為開頭的最大子陣列和 R[i]。
則以 i 為修改位置時，所求的最大子陣列和為 L[i] + R[i] - A[i] + B[i]。
"""

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert len(A) == len(B) == n

    L = [float('-inf')] * n
    for i in range(n):
        L[i] = L[i - 1] + A[i] if i > 0 and L[i - 1] > 0 else A[i]
    R = [float('-inf')] * n
    for i in range(n - 1, -1, -1):
        R[i] = R[i + 1] + A[i] if i < n - 1 and R[i + 1] > 0 else A[i]

    ans = max(L)
    if k & 1:
        ans = max(ans, max(l + r - a + b for l, r, a, b in zip(L, R, A, B)))
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()