T = int(input())

for tc in range(1, T+1):
    n = int(input().split()[2])
    mtrx = [list(map(int, input().split())) for _ in range(n)]

    flag = True
    for i in range(n):
        for j in range(n):
            if mtrx[i][j] < 0 or mtrx[i][j] != mtrx[n - 1 - i][n - 1 - j]:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(f"Test #{tc}: Symmetric.")
    else:
        print(f"Test #{tc}: Non-symmetric.")