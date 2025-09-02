N = int(input())
covers  = [list(map(int, input().split(" "))) for _ in range(N)]

matrix = [[0 for _ in range(101)] for _ in range(101)]
for cover in covers:
    X1, X2, Y1, Y2 = cover
    for x in range(X1, X2):
        for y in range(Y1, Y2):
            matrix[x][y] = 1
print(sum([sum(row) for row in matrix]))
# ans = 0
# # 對每個Y軸，找出X軸的左右邊界
# y_axis = {}
# for cover in covers:
#     X1, X2, Y1, Y2 = cover
#     for y in range(Y1, Y2+1):
#         if y not in y_axis:
#             y_axis[y] = [X1, X2]
#         else:
#             y_axis[y][0] = min(y_axis[y][0], X1)
#             y_axis[y][1] = max(y_axis[y][1], X2)
# ys = sorted(y_axis.keys())
# print(y_axis)

# for i in range(1, len(ys)):
#     print(y_axis[ys[i]])
# for i in range(1, len(ys)):
#     l1, r1 = y_axis[ys[i-1]]
#     l2, r2 = y_axis[ys[i]]
#     # print(min(r1, r2), max(l1, l2))
#     ans += min(r1, r2) - max(l1, l2)

# print(ans)