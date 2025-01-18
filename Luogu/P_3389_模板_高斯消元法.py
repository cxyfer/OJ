n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

def gauss_elimination(mat, eps=1e-6):
    for i in range(n):
        pivot = i
        for j in range(i + 1, n):
            if abs(mat[j][i]) > abs(mat[pivot][i]):
                pivot = j
        
        if abs(mat[pivot][i]) < eps:
            return -1
        
        if pivot != i:
            mat[i], mat[pivot] = mat[pivot], mat[i]
        
        for j in range(i + 1, n):
            factor = mat[j][i] / mat[i][i]
            for k in range(i, n + 1):
                mat[j][k] -= factor * mat[i][k]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_val = sum(mat[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (mat[i][n] - sum_val) / mat[i][i]

    return x

res = gauss_elimination(mat)
if res != -1:
    for val in res:
        print("{:.2f}".format(val))
else:
    print("No Solution")