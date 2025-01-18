# 數獨
rows = [[0] * 10 for _ in range(9)] # rows[i][j] 代表第 i 列有沒有數字 j
cols = [[0] * 10 for _ in range(9)] # cols[i][j] 代表第 i 行有沒有數字 j
sqrs = [[0] * 10 for _ in range(9)] # sqrs[i][j] 代表第 i 個 3x3 的方格有沒有數字 j

for i in range(9):
    M = list(map(int, input().split()))
    for j in range(9):
        x = M[j]
        if rows[i][x] or cols[j][x] or sqrs[i//3*3+j//3][x]:
            print("No")
            exit()
        rows[i][x] = 1
        cols[j][x] = 1
        sqrs[i//3*3+j//3][M[j]] = 1
print("Yes")

# from collections import defaultdict

# M = [list(map(int, input().split())) for _ in range(9)]

# flag = True
# for i in range(9):
#     cnt = defaultdict(int)
#     for j in range(9):
#         cnt[M[i][j]] += 1
#     for j in range(1, 10):
#         if cnt[j] != 1:
#             print("No")
#             exit()
# for i in range(9):
#     cnt = defaultdict(int)
#     for j in range(9):
#         cnt[M[j][i]] += 1
#     for j in range(1, 10):
#         if cnt[j] != 1:
#             print("No")
#             exit()
# for i in range(3):
#     if not flag:
#         break
#     for j in range(3):
#         cnt = defaultdict(int)
#         for k in range(3):
#             for l in range(3):
#                 cnt[M[i*3+k][j*3+l]] += 1
#         for k in range(1, 10):
#             if cnt[k] != 1:
#                 print("No")
#                 exit()
# print("Yes")