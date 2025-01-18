""" UVA-11360: Have Fun with Matrices
    模擬(Simulation)
    已於 UVA, CPE 測試通過 (無 ZeroJudge)

    一個可能的優化：
    - inc, dec 可留待最後一起處理
"""
t = int(input())

for kase in range(1, t+1):
    n = int(input())
    mtrx = [list(map(int, input())) for _ in range(n)]
    m = int(input()) # number of operations
    for _ in range(m):
        op, *args = input().split()
        if op == 'row':
            a, b = map(int, args)
            mtrx[a-1], mtrx[b-1] = mtrx[b-1], mtrx[a-1]
        elif op == 'col':
            a, b = map(int, args)
            for i in range(n):
                mtrx[i][a-1], mtrx[i][b-1] = mtrx[i][b-1], mtrx[i][a-1]
        elif op == 'inc':
            for i in range(n):
                for j in range(n):
                    mtrx[i][j] = (mtrx[i][j] + 1) % 10
        elif op == 'dec':
            for i in range(n):
                for j in range(n):
                    mtrx[i][j] = (mtrx[i][j] - 1) % 10
        elif op == 'transpose':
            for i in range(n):
                for j in range(i+1, n):
                    mtrx[i][j], mtrx[j][i] = mtrx[j][i], mtrx[i][j]
    print(f"Case #{kase}")
    for row in mtrx:
        print(''.join(map(str, row)))
    print() # print a blank line after each test case