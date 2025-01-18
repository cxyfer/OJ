def gauss_elimination(mat, ans, eps=1e-6):
    mat = [row[:] for row in mat[:n]]  # call by value
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
data = [list(map(float, input().split())) for _ in range(n + 1)]

mat = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    m, *args, w = data[i]
    for j in map(lambda x: int(x) - 1, args):
        mat[i][j] = 1
    mat[i][n] = w

ans, ans_cnt = -1, 0
for absent in range(n + 1):
    res = [0] * n
    mat[absent], mat[n] = mat[n], mat[absent]
    gauss_elimination(mat, res)
    mat[n], mat[absent] = mat[absent], mat[n]

    mx_idx = mx_cnt = 0
    for i, x in enumerate(res):
        if x <= 0 or int(x) != x:
            break
        if x > res[mx_idx]:
            mx_idx = i
            mx_cnt = 1
        elif x == res[mx_idx]:
            mx_cnt += 1
    else:
        if mx_cnt > 1:
            continue
        ans = mx_idx + 1
        ans_cnt += 1

if ans == -1 or ans_cnt > 1:
    print("illegal")
else:
    print(ans)