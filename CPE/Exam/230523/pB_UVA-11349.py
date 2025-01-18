T = int(input())

for kase in range(1, T+1):
    n = int(input().split()[2])
    mat = [list(map(int, input().split())) for _ in range(n)]

    flag = True
    for i in range(n):
        for j in range(n):
            # 雖然檢查是否對稱只需要檢查上半部即可，但還是要檢查是否有負數
            if mat[i][j] < 0 or mat[i][j] != mat[n - 1 - i][n - 1 - j]:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        print(f"Test #{kase}: Symmetric.")
    else:
        print(f"Test #{kase}: Non-symmetric.")