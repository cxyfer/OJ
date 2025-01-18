n = int(input())
mat = [list(map(float, input().split())) for _ in range(n)]

def gauss_elimination(mat, ans, eps=1e-6):
    # Forward elimination
    rank = 0
    for col in range(n):
        # Find pivot
        pivot = rank
        for i in range(rank + 1, n):
            if abs(mat[i][col]) > abs(mat[pivot][col]):
                pivot = i
        
        # If current column is all zeros, continue to next column
        if abs(mat[pivot][col]) < eps:
            continue
        
        # Swap rows if necessary
        if pivot != rank:
            mat[rank], mat[pivot] = mat[pivot], mat[rank]
        
        # Eliminate column
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
    
    # Back substitution
    for i in range(n - 1, -1, -1):
        sum_val = sum(mat[i][j] * ans[j] for j in range(i + 1, n))
        ans[i] = (mat[i][n] - sum_val) / mat[i][i]
        if abs(ans[i]) < eps:
            ans[i] = 0
    return 1  # Unique solution

ans = [0] * n
flag = gauss_elimination(mat, ans)

if flag == -1:
    print(-1)  # No solution
elif flag == 0:
    print(0)   # Infinite solutions
else:
    for i, x in enumerate(ans):
        print(f"x{i+1}={x:.2f}")