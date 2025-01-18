"""
以三維為例：
令 (x0, y0, z0) 為球心，(xi, yi, zi) 為球上的一點
(x1-x0)^2 + (y1-y0)^2 + (z1-z0)^2 = (x2-x0)^2 + (y2-y0)^2 + (z2-z0)^2

   x1^2 - 2x1x0 + x0^2 + y1^2 - 2y1y0 + y0^2 + z1^2 - 2z1z0 + z0^2
 = x2^2 - 2x2x0 + x0^2 + y2^2 - 2y2y0 + y0^2 + z2^2 - 2z2z0 + z0^2
 => 2x2x0 - 2x1x0 + 2y2y0 - 2y1y0 + 2z2z0 - 2z1z0 = x2^2 - x1^2 + y2^2 - y1^2 + z2^2 - z1^2

有 n + 1 個點，可列出 n 個方程式，使用高斯消去法求解
"""

def gauss_elimination(mat, ans, eps=1e-6):
    rank = 0
    for col in range(n):
        pivot = rank
        for i in range(rank + 1, n):
            if abs(mat[i][col]) > abs(mat[pivot][col]):
                pivot = i
        
        if abs(mat[pivot][col]) < eps:
            continue
        
        if pivot != rank:
            mat[rank], mat[pivot] = mat[pivot], mat[rank]
        
        for i in range(rank + 1, n):
            if abs(mat[i][col]) < eps:
                continue
            factor = mat[i][col] / mat[rank][col]
            for k in range(col, n + 1):
                mat[i][k] -= mat[rank][k] * factor
        
        rank += 1
    
    for i in range(rank, n):
        if abs(mat[i][n]) > eps:
            return -1  # No solution
    
    if rank < n:
        return 0  # Infinite solutions
    
    for i in range(n - 1, -1, -1):
        sum_val = sum(mat[i][j] * ans[j] for j in range(i + 1, n))
        ans[i] = (mat[i][n] - sum_val) / mat[i][i]
        if abs(ans[i]) < eps:
            ans[i] = 0
    return 1  # Unique solution

n = int(input())
points = [list(map(float, input().split())) for _ in range(n + 1)]

mat = [[0] * (n + 1) for _ in range(n)]
for i in range(n):
    p1, p2 = points[i], points[i + 1]
    for j in range(n):
        mat[i][j] = 2 * (p2[j] - p1[j])
    mat[i][n] = sum(p2[j] ** 2 - p1[j] ** 2 for j in range(n))

ans = [0] * n
gauss_elimination(mat, ans)

print(*map(lambda x: f"{x:.3f}", ans))