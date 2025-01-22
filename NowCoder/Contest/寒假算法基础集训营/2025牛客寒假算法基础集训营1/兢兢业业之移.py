def check(matrix):
    n = len(matrix)
    h = n // 2
    for i in range(n):
        for j in range(n):
            if i < h and j < h:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    mtrx = [list(map(int, list(input()))) for _ in range(n)]

    ans = []
    for r2 in range(n // 2):
        for c2 in range(n // 2):
            if mtrx[r2][c2] == 1:
                continue
            r1, c1 = -1, -1
            for rr in range(n):
                for cc in range(n):
                    if rr < r2 and cc < n // 2:
                        continue
                    if rr == r2 and cc < c2:
                        continue
                    if mtrx[rr][cc] == 1:
                        r1, c1 = rr, cc
                        break
                if r1 != -1 and c1 != -1:
                    break

            # assert r1 != -1 and c1 != -1
            # a, b, c, d = r1, c1, r2, c2

            while r1 < r2:
                ans.append((r1, c1, r1 + 1, c1))
                mtrx[r1][c1], mtrx[r1 + 1][c1] = mtrx[r1 + 1][c1], mtrx[r1][c1]
                r1 += 1
            while c1 > c2:
                ans.append((r1, c1, r1, c1 - 1))
                mtrx[r1][c1], mtrx[r1][c1 - 1] = mtrx[r1][c1 - 1], mtrx[r1][c1]
                c1 -= 1
            while c1 < c2:
                ans.append((r1, c1, r1, c1 + 1))
                mtrx[r1][c1], mtrx[r1][c1 + 1] = mtrx[r1][c1 + 1], mtrx[r1][c1]
                c1 += 1
            while r1 > r2:
                ans.append((r1, c1, r1 - 1, c1))
                mtrx[r1][c1], mtrx[r1 - 1][c1] = mtrx[r1 - 1][c1], mtrx[r1][c1]
                r1 -= 1
  
            # print(f"after move {a} {b} to {c} {d}")
            # for row in mtrx:
            #     print(*row)

    print(len(ans))
    for op in ans:
        print(*map(lambda x: x+1, op))
    # print(check(mtrx))