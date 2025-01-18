def dfs(n):
    if n == 0: # n = [0, 6]
        return [['#']]
    if n == 1:
        return [['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#']]
    mat = [['.'] * int(3 ** n) for _ in range(int(3 ** n))]
    pre = dfs(n - 1)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for x in range(int(3 ** (n - 1))):
                for y in range(int(3 ** (n - 1))):
                    mat[i * int(3 ** (n-1)) + x][j * int(3 ** (n-1)) + y] = pre[x][y]
    return mat

n = int(input())
for row in dfs(n):
    print(''.join(row))